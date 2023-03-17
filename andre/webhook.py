from urllib import response
from flask import Flask, request, jsonify
#import model


app = Flask(__name__)

@app.route('/whats', methods=['POST'])
def main():
    data = request.get_json(silent=True)
    wMessage = data.get('message')[0]

    if wMessage['key']['fromMe'] == False:
         model.detectType(wMessage)

    print("\n\n-------------------------------------\n\n")
    print(data)

    return jsonify({})


# run Flask app
if __name__ == "__main__":
    app.debug = False
    app.run()
    
    
    
