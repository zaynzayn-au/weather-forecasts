import pyowm

owm = pyowm.OWM('3d2e01eac301a7de4720f37117917f56')

def get_forecast():
	fcst = owm.three_hours_forecast('Sydney')
	forecast_message = '\n\n***阳间天气预测***\n\n\n'

	if fcst.will_have_rain():
		for f in fcst.when_rain():
			print(f)

if __name__ == '__main__':
	get_forecast()