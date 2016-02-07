//REQUIRES
//	Charts.js


var charts = []


//creates a chart's data structure from an array of labels and raw data
function formatData(labels, chart_data){
	return {
		labels: labels,
		datasets: [
			{
				label: "",
				fillColor: "rgba(220,220,220,0.2)",
				strokeColor: "rgba(220,220,220,1)",
				pointColor: "rgba(220,220,220,1)",
				pointStrokeColor: "#fff",
				pointHighlightFill: "#fff",
				pointHighlightStroke: "rgba(220,220,220,1)",
				data: chart_data
			}
		]
	}
}


function getChartContext(chart_id){
	return $("#" + chart_id).get(0).getContext("2d");
}


function addLineChart(chart_id, data){
	charts.push({
		key: chart_id,
		value: new Chart(getChartContext(chart_id)).Line(data, {
			scaleLineColor: "rgba(200,200,200,1)",
			scaleFontColor: "rgba(200,200,200,1)",
			scaleOverride: true,
			scaleSteps: 10,
			scaleStepWidth: 10,
			scaleStartValue: 0,
			scaleBeginsAtZero: true,
			animationSteps: 15
		})
	});
}
