from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the Random Forest CLassifier model
filename = 'first_innings_lr_model.pkl'
regressor = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    final_arr = np.zeros(30, dtype=np.int)

    if request.method == 'POST':

        venue = request.form['venue']
        if venue == 'Brabourne Stadium':
            final_arr[0] = 1
        if venue == 'Buffalo Park':
            final_arr[1] = 1
        if venue == 'De Beers Diamond Oval':
            final_arr[2] = 1
        if venue == 'Dr DY Patil Sports Academy':
            final_arr[3] = 1
        if venue == 'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium':
            final_arr[4] = 1
        if venue == 'Dubai International Cricket Stadium':
            final_arr[5] = 1
        if venue == 'Eden Gardens':
            final_arr[6] = 1
        if venue == 'Feroz Shah Kotla':
            final_arr[7] = 1
        if venue == 'Himachal Pradesh Cricket Association Stadium':
            final_arr[8] = 1
        if venue == 'Holkar Cricket Stadium':
            final_arr[9] = 1
        if venue == 'JSCA International Stadium Complex':
            final_arr[10] = 1
        if venue == 'Kingsmead':
            final_arr[11] = 1
        if venue == 'M Chinnaswamy Stadium':
            final_arr[12] = 1
        if venue == 'MA Chidambaram Stadium, Chepauk':
            final_arr[13] = 1
        if venue == 'Maharashtra Cricket Association Stadium':
            final_arr[14] = 1
        if venue == 'New Wanderers Stadium':
            final_arr[15] = 1
        if venue == 'Newlands':
            final_arr[16] = 1
        if venue == 'OUTsurance Oval':
            final_arr[17] = 1
        if venue == 'Punjab Cricket Association IS Bindra Stadium, Mohali':
            final_arr[18] = 1
        if venue == 'Punjab Cricket Association Stadium, Mohali':
            final_arr[19] = 1
        if venue == 'Rajiv Gandhi International Stadium, Uppal':
            final_arr[20] = 1
        if venue == 'Sardar Patel Stadium, Motera':
            final_arr[21] = 1
        if venue == 'Sawai Mansingh Stadium':
            final_arr[22] = 1
        if venue == 'Shaheed Veer Narayan Singh International Stadium':
            final_arr[23] = 1
        if venue == 'Sharjah Cricket Stadium':
            final_arr[24] = 1
        if venue == 'Sheikh Zayed Stadium':
            final_arr[25] = 1
        if venue == "St George's Park":
            final_arr[26] = 1
        if venue == 'Subrata Roy Sahara Stadium':
            final_arr[27] = 1
        if venue == 'SuperSport Park':
            final_arr[28] = 1
        if venue == 'Wankhede Stadium':
            final_arr[29] = 1

        batting_team = request.form['batting-team']
        bat_arr = np.zeros(7, dtype=np.int)
        if batting_team == 'Delhi Daredevils':
            bat_arr[0] = 1
        elif batting_team == 'Kings XI Punjab':
            bat_arr[1] = 1
        elif batting_team == 'Kolkata Knight Riders':
            bat_arr[2] = 1
        elif batting_team == 'Mumbai Indians':
            bat_arr[3] = 1
        elif batting_team == 'Rajasthan Royals':
            bat_arr[4] = 1
        elif batting_team == 'Royal Challengers Bangalore':
            bat_arr[5] = 1
        elif batting_team == 'Sunrisers Hyderabad':
            bat_arr[6] = 1
        final_arr = np.append(final_arr, bat_arr)

        bowling_team = request.form['bowling-team']
        bowl_arr = np.zeros(7, dtype=np.int)
        if bowling_team == 'Delhi Daredevils':
            bowl_arr[0] = 1
        elif bowling_team == 'Kings XI Punjab':
            bowl_arr[1] = 1
        elif bowling_team == 'Kolkata Knight Riders':
            bowl_arr[2] = 1
        elif bowling_team == 'Mumbai Indians':
            bowl_arr[3] = 1
        elif bowling_team == 'Rajasthan Royals':
            bowl_arr[4] = 1
        elif bowling_team == 'Royal Challengers Bangalore':
            bowl_arr[5] = 1
        elif bowling_team == 'Sunrisers Hyderabad':
            bowl_arr[6] = 1
        final_arr = np.append(final_arr, bowl_arr)


        overs = float(request.form['overs'])
        runs = int(request.form['runs'])
        wickets = int(request.form['wickets'])
        runs_in_prev_5 = int(request.form['runs_in_prev_5'])
        wickets_in_prev_5 = int(request.form['wickets_in_prev_5'])

        final_arr = np.append([runs, wickets, overs, runs_in_prev_5, wickets_in_prev_5], final_arr)
        my_prediction = int(regressor.predict([final_arr])[0])

        return render_template('results.html', lower_limit = my_prediction-10, upper_limit = my_prediction+5)



if __name__ == '__main__':
	app.run(debug=True)
