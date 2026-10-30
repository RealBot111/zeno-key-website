from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Key</title>
  <style>
    *{box-sizing:border-box}
    body{
      margin:0; min-height:100vh; display:flex; align-items:center;
      justify-content:center; background:#0b0b0f; color:#fff;
      font-family:Arial,sans-serif;
    }
    .box{
      width:min(90%,420px); padding:30px; text-align:center;
      background:#17171d; border:1px solid #2d2d36;
      border-radius:22px; box-shadow:0 20px 60px #0008;
    }
    h1{margin:0 0 22px;font-size:28px}
    .key{
      padding:16px; margin-bottom:18px; border-radius:12px;
      background:#0d0d12; color:#00ff88; font-size:20px;
      font-weight:700; letter-spacing:1px; user-select:all;
    }
    button{
      width:100%; border:0; border-radius:12px; padding:15px;
      background:#00ff88; color:#06140d; font-size:17px;
      font-weight:700; cursor:pointer;
    }
    button:active{transform:scale(.98)}
    #msg{height:22px;margin-top:14px;color:#00ff88;font-weight:600}
  </style>
</head>
<body>
  <div class="box">
    <h1>Your Key</h1>
    <div class="key" id="key">PAPA-XYZ-123</div>
    <button onclick="copyKey()">Copy Key</button>
    <div id="msg"></div>
  </div>
  <script>
    async function copyKey(){
      const key = document.getElementById("key").innerText;
      try {
        await navigator.clipboard.writeText(key);
      } catch(e) {
        const area = document.createElement("textarea");
        area.value = key;
        document.body.appendChild(area);
        area.select();
        document.execCommand("copy");
        area.remove();
      }
      document.getElementById("msg").innerText = "✓ Key Copied!";
    }
  </script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
