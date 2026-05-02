from flask import Flask, render_template_string

app = Flask(__name__)

WELCOME_PAGE = """
<!doctype html>
<html lang="es">
  <head>
    <meta charset="utf-8">
    <title>Bienvenida</title>
    <style>
      body {
        font-family: Arial, sans-serif;
        background: #f4f7fb;
        color: #333;
        text-align: center;
        padding: 4rem;
      }
      .card {
        background: white;
        border-radius: 12px;
        box-shadow: 0 16px 40px rgba(0, 0, 0, 0.08);
        display: inline-block;
        padding: 2rem 3rem;
        max-width: 520px;
      }
      h1 {
        color: #0366d6;
        margin-bottom: 0.5rem;
      }
      p {
        font-size: 1.05rem;
        line-height: 1.6;
      }
    </style>
  </head>
  <body>
    <div class="card">
      <h1>¡Bienvenido a Flask!</h1>
      <p>Esta es una aplicación web simple creada con Python y Flask.</p>
      <p>Visita <strong>/</strong> para ver esta página de bienvenida.</p>
    </div>
  </body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(WELCOME_PAGE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
