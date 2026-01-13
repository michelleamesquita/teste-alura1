from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <html>
        <body>
            <h1>Vulnerável a XSS</h1>
            <form action="/greet" method="GET">
                <input type="text" name="name" placeholder="Seu nome">
                <button type="submit">Enviar</button>
            </form>
        </body>
    </html>
    '''

@app.route('/greet')
def greet():
    # VULNERABILIDADE XSS: entrada do usuário não é sanitizada
    name = request.args.get('name', 'Visitante')
    
    # Renderiza diretamente sem escape - VULN!
    html = f'''
    <html>
        <body>
            <h1>Olá, {name}!</h1>
            <a href="/">Voltar</a>
        </body>
    </html>
    '''
    return render_template_string(html)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
