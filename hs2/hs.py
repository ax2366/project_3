
from flask import Flask
from flask import Blueprint, render_template, request
import pickle
import pandas as pd

# model = None
# with open('AI_15_이새벽_Section3.pkl','rb') as pickle_file:
#     model = pickle.load(pickle_file)

# print(model)



# Flask factory
def create_app():
    app = Flask(__name__)
    # @app.route('/')
    # def hs():
    #     return render_template('hs.html')    
    
    @app.route('/') #/search
    def search():
        return render_template('search.html')

    @app.route('/result', methods = ['POST'])
    def result():
        column_list=['temp', 'rain']

        a = request.form.get('temp')
        b = request.form.get('rain')
   
      
        
        data = [int(a),int(b)]
        X_test = pd.DataFrame([data], columns = column_list)

        with open('AI_15_이새벽_Section3.pkl', 'rb') as pickle_file:
            model = pickle.load(pickle_file)
            y_pred = model.predict(X_test)[0]
            re = round(abs(y_pred),2)
          

        return render_template('result.html', result_ = re)
    
    return app




if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)



# FLASK_APP=hs.py FLASK_DEBUG=1 flask run