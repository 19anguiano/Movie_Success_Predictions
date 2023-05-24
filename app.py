from flask import Flask, render_template, request
import pickle

app=Flask(__name__)

with open('assets/lr.pkl', 'rb') as f: 
	lr=pickle.load(f)

# with open('assets/scaler.pkl', 'rb') as f: 
# 	scaler=pickle.load(f)

# def preprocessing(): 
# 	query database to retrieve data
# 	scaling data to what the model expects
# 	X_scaled=scaler.transform(X)
# 	return input_array

@app.route('/', methods=['GET', 'POST'])
def home(): 
	# return render_template('index_1.html')
	
	# return render_template('index_2.html', output='hard-coded 17')
	
	# x1=request.form.get('x1')
	# x2=request.form.get('x2')
	# model_output=lr.predict([(x1, x2)])
	# return render_template('index_2.html', output=f'Class {model_output[0]}')

	if request.method=='POST': 
		x1=request.form.get('x1')
		x2=request.form.get('x2')
		model_output=lr.predict([(x1, x2)])
		return render_template('index_2.html', output=f'Class {model_output[0]}')
		# return render_template('index_2.html', output='THIS IS A POST REQUEST')
	else: 
		return render_template('index_2.html')

if __name__=='__main__': 
	app.run()