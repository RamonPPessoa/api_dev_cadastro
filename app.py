from flask import Flask,jsonify,request
import json
app = Flask(__name__)

devs =[
    {'name': 'Ramon',
      'habilidades': ['C Sharp','Python','Java']
    },
    {'name':'Pessoa',
     'habilidades':['Postgres','SQLServer']}
]

@app.route('/dev/<int:id>/',methods=['GET','POST'])
def desenvolvedor(id):
      if request.method == 'GET':
        desenvolvedor = devs[id]
        print(desenvolvedor)
        return jsonify(desenvolvedor)
      elif request.method == 'PUT':
           dados = json.loads(request.data)
           devs[id] = dados
           return jsonify(dados)

 

        

if __name__ == '__main__':
    app.run(debug=True)