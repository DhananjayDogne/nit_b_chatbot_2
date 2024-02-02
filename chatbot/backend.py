from flask import Flask, request, jsonify, render_template
from ast import literal_eval
from pymongo import MongoClient
from flask_cors import CORS
import openai


app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "*"}})


# database connection
client=MongoClient('mongodb+srv://dhananjaydogne:DD@cluster0.q565lol.mongodb.net/?retryWrites=true&w=majority')
db=client.get_database('manit')

# opportunity 
@app.route('/opportunity', methods=['GET','POST'])
def add_opportunity():
    
    if request.method == 'POST':
        user_input = request.data
        user_input=literal_eval(user_input.decode('utf-8'))
        title = user_input['title']
        description = user_input['description']
        location=user_input['location']
        deadline=user_input['deadline']
       

        # Store data in MongoDB database
        db.opportunity.insert_one({'title':title, 'description':description,"location":location, 'deadline':deadline})
        
        
        return jsonify({'message': 'Data received successfully'}), 200
    
    data = jsonify(list(db.opportunity.find({}, {'_id': 0})))
    print(data)
    return data, 200


#  chat bot 

@app.route("/chat", methods=["GET", "POST"])
def CustomChatGPT():
    openai.api_key = "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"

    messages = [{"role": "system", "content": "You are a financial experts that specializes in real estate investment and negotiation"}]

    user_input=request.data
    user_input=literal_eval(user_input.decode('utf-8'))
    user_input=user_input["user_input"]
    print(request.data)
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    print(ChatGPT_reply)
    return jsonify({"response":ChatGPT_reply})
    
if __name__ == '__main__':
    app.run(debug=True)
