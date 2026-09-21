#@title CTI Dashboard - No Ngrok Needed
!pip install flask -q

from flask import Flask, request, jsonify, render_template_string
from threading import Thread
import datetime, random, csv, io
from google.colab import output
from IPython.display import display, HTML as HTMLD

app = Flask(__name__)
DB = []

def check_threat(ip):
    score = random.randint(0,100)
    level = "High" if score>75 else "Medium" if score>45 else "Low" if score>20 else "Clean"
    return {"ip":ip,"threat_level":level,"abuse_score":score,
            "country":random.choice(["IN","US","RU","CN"]),
            "ioc":random.choice(["Malware IP","Brute Force","Spam","Phishing"]),
            "time":datetime.datetime.now().strftime("%H:%M:%S")}

PAGE = """
<html><head><meta name="viewport" content="width=device-width, initial-scale=1">
<style>body{font-family:sans-serif;background:#0f172a;color:#fff;padding:12px}
.card{background:#1e293b;padding:12px;border-radius:10px;margin:10px 0}
input,button{padding:10px;border-radius:8px;border:none} button{background:#38bdf8;font-weight:bold}
.High{color:#ff4d4d} .Medium{color:#ffcc00} .Low,.Clean{color:#4dff88}
table{width:100%} td,th{padding:6px;border-bottom:1px solid #334155;font-size:14px}
</style></head><body>
<h3>🛡️ Cyber Threat Intel Dashboard</h3>
<div class="card">
<input id="ip" placeholder="8.8.8.8" value="8.8.8.8">
<button onclick="check()">Check Threat</button>
<button onclick="location.href='/export'">Export CSV</button>
</div>
<div id="res" class="card">Result...</div>
<div class="card"><table id="tbl"></table></div>
<script>
async function check(){
 let ip=document.getElementById('ip').value;
 let r=await fetch('/check?ip='+ip); let d=await r.json();
 document.getElementById('res').innerHTML=`<b>${d.ip}</b> - <span class=${d.threat_level}>${d.threat_level} (${d.abuse_score})</span> | ${d.ioc} | ${d.time}`;
 load();
}
async function load(){
 let r=await fetch('/history'); let data=await r.json();
 let h='<tr><th>IP</th><th>Level</th><th>Score</th></tr>';
 data.forEach(x=>{h+=`<tr><td>${x.ip}</td><td class=${x.threat_level}>${x.threat_level}</td><td>${x.abuse_score}</td></tr>`});
 document.getElementById('tbl').innerHTML=h;
}
load(); setInterval(load,3000);
</script></body></html>
"""

@app.route('/')
def home(): return render_template_string(PAGE)
@app.route('/check')
def chk():
    ip=request.args.get('ip','8.8.8.8'); d=check_threat(ip); DB.append(d); return jsonify(d)
@app.route('/history')
def hist(): return jsonify(DB[::-1][:20])
@app.route('/export')
def exp():
    out=io.StringIO(); w=csv.DictWriter(out, fieldnames=["ip","threat_level","abuse_score","country","ioc","time"]); w.writeheader(); w.writerows(DB)
    return out.getvalue(),200,{'Content-Type':'text/csv','Content-Disposition':'attachment;filename=report.csv'}

def run(): app.run(port=5000)
Thread(target=run, daemon=True).start()

output.serve_kernel_port_as_window(5000)
display(HTMLD('<p>👆 Paina vachina link click chey, lekapothe <b>https://'+output.eval_js('google.colab.kernel.proxyPort(5000)')+' </b> open avvaledante, kinda preview lo chudu</p>'))
print("Dashboard running on port 5000 - Paina blue link vastundi, click chey!")