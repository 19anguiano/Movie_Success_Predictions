from flask import Flask, render_template, request
import pickle

app=Flask(__name__)



# Put in weighted rating score for each genre
History_r = 6.911842
Romance_r = 6.488455
Action_r = 6.189252
Documentary_r = 6.800000
Fantasy_r = 6.260093
Thriller_r = 6.257021
Family_r = 6.319114
Drama_r = 6.708864
Western_r = 6.753846
Crime_r = 6.493427
ScienceFiction_r = 6.206693
War_r = 6.879545
Mystery_r = 6.474702
Music_r = 6.553211
Animation_r = 6.573200
Comedy_r = 6.217584
Adventure_r = 6.321212
Horror_r = 5.896101

# Put in weighted popularity score for each genre
History_p = 11.118591
Romance_p = 10.599035
Action_p = 14.323888
Documentary_p = 9.266240
Fantasy_p = 15.544317
Thriller_p = 12.003043
Family_p = 14.680515
Drama_p = 11.169210
Western_p = 12.306263
Crime_p = 11.621943
ScienceFiction_p = 15.198877
War_p = 12.627602
Mystery_p = 11.905200
Music_p = 10.468263
Animation_p = 16.074660
Comedy_p = 11.269783
Adventure_p = 15.738319
Horror_p = 10.888739

with open('assets/model_rfc.pkl', 'rb') as f: 
	model_rfc=pickle.load(f)

with open('assets/scaler.pkl', 'rb') as f: 
	scaler=pickle.load(f)

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
		anticipated_vote_rating = []
		anticipated_popularity = []
		post_streaming = 1
		fl = 0
		print(request.form)
		budget=int(request.form.get('budget'))
		runtime=int(request.form.get('runtime'))
		month=int(request.form.get('month'))
		en=int(request.form.get('en'))
		if en == 0:
			fl = 1
		history=int(request.form.get('History'))
		if history == 1:
			anticipated_vote_rating.append(History_r)
			anticipated_popularity.append(History_p)
		romance=int(request.form.get('Romance'))
		if romance == 1:
			anticipated_vote_rating.append(Romance_r)
			anticipated_popularity.append(Romance_p)
		action=int(request.form.get('Action'))
		if action == 1:
			anticipated_vote_rating.append(Action_r)
			anticipated_popularity.append(Action_p)
		documentary=int(request.form.get('Documentary'))
		if documentary == 1:
			anticipated_vote_rating.append(Documentary_r)
			anticipated_popularity.append(Documentary_p)
		fantasy=int(request.form.get('Fantasy'))
		if fantasy == 1:
			anticipated_vote_rating.append(Fantasy_r)
			anticipated_popularity.append(Fantasy_p)
		thriller=int(request.form.get('Thriller'))
		if thriller == 1:
			anticipated_vote_rating.append(Thriller_r)
			anticipated_popularity.append(Thriller_p)
		family=int(request.form.get('Family'))
		if family == 1:
			anticipated_vote_rating.append(Family_r)
			anticipated_popularity.append(Family_p)
		drama=int(request.form.get('Drama'))
		if drama == 1:
			anticipated_vote_rating.append(Drama_r)
			anticipated_popularity.append(Drama_p)
		western=int(request.form.get('Western'))
		if western == 1:
			anticipated_vote_rating.append(Western_r)
			anticipated_popularity.append(Western_p)
		crime=int(request.form.get('Crime'))
		if crime == 1:
			anticipated_vote_rating.append(Crime_r)
			anticipated_popularity.append(Crime_p)
		sci_fi=int(request.form.get('Science Fiction'))
		if sci_fi == 1:
			anticipated_vote_rating.append(ScienceFiction_r)
			anticipated_popularity.append(ScienceFiction_p)
		war=int(request.form.get('War'))
		if war == 1:
			anticipated_vote_rating.append(War_r)
			anticipated_popularity.append(War_p)
		mystery=int(request.form.get('Mystery'))
		if mystery == 1:
			anticipated_vote_rating.append(Mystery_r)
			anticipated_popularity.append(Mystery_p)
		music=int(request.form.get('Music'))
		if music == 1:
			anticipated_vote_rating.append(Music_r)
			anticipated_popularity.append(Music_p)
		animation=int(request.form.get('Animation'))
		if animation == 1:
			anticipated_vote_rating.append(Animation_r)
			anticipated_popularity.append(Animation_p)
		comedy=int(request.form.get('Comedy'))
		if comedy == 1:
			anticipated_vote_rating.append(Comedy_r)
			anticipated_popularity.append(Comedy_p)
		adventure=int(request.form.get('Adventure'))
		if adventure == 1:
			anticipated_vote_rating.append(Adventure_r)
			anticipated_popularity.append(Adventure_p)
		horror=int(request.form.get('Horror'))
		if horror == 1:
			anticipated_vote_rating.append(Horror_r)
			anticipated_popularity.append(Horror_p)
		print(anticipated_vote_rating)
		
		anticipated_vote_rating_m = sum(anticipated_vote_rating)/len(anticipated_vote_rating)
		anticipated_popularity_m = sum(anticipated_popularity)/len(anticipated_popularity)
		
		input_array = [[budget, runtime, month, post_streaming, history, romance, 
		 action, documentary, fantasy, thriller, family, drama, western, crime,
		 sci_fi, war, mystery, music, animation, comedy, adventure, horror, en, fl,
		 anticipated_vote_rating_m, anticipated_popularity_m]]
		
		input_scaled=scaler.transform(input_array)
		print(input_scaled)
		model_output=model_rfc.predict(input_scaled)

		return render_template('index.html', output=f'Class {model_output[0]}')
		
	else: 
		return render_template('index.html')

if __name__=='__main__': 
	app.run()