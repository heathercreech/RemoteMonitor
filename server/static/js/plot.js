//REQUIRES
//	Charts.js


var charts = {}
var max_points = 10;


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


//generates all the elements required to display a chart -- value_source is where the data came from (i.e. 'cpu') and value_type is what the value represents (i.e. 'usage')
function generateChart(value_source, value_type){
	var chart_container = document.createElement("div");
	chart_container.className = "app-item";
	
	chart_container.appendChild(generateChartHeader(value_source, value_type));
	chart_container.appendChild(generateChartCanvas(value_source, value_type));
	
	return chart_container;
}


//generates a charts header -- value_source is where the data came from (i.e. 'cpu') and value_type is what the value represents (i.e. 'usage')
function generateChartHeader(value_source, value_type){
	var chart_header = document.createElement("h3");
	chart_header.innerHTML = value_source + " " + value_type;
	return chart_header;
}


//generates a charts canvas -- value_source is where the data came from (i.e. 'cpu') and value_type is what the value represents (i.e. 'usage')
function generateChartCanvas(value_source, value_type){
	var chart_canvas = document.createElement("canvas");
	var sq_gph = 200;
	
	chart_canvas.width = sq_gph;
	chart_canvas.height = sq_gph;
	
	
	//generate the id of the chart
	var chart_id = value_source + "_" + value_type;
	
	chart_canvas.setAttribute("id", chart_id);
	console.log(chart_canvas);
	//chart_canvas.getContext("2d");
	addLineChart(chart_canvas, formatData([], []));
	
	return chart_canvas;
}


//returns a chart's canvas context
function getChartContext(chart_canvas){
	return chart_canvas.getContext("2d");
}


//sets a line chart's visual options and adds it to the charts array
function addLineChart(chart_canvas, data){
	charts[chart_canvas.getAttribute("id")] = new Chart(getChartContext(chart_canvas)).Line(data, {
			scaleLineColor: "rgba(200,200,200,1)",
			scaleFontColor: "rgba(200,200,200,1)",
		});
}


//adds a data point to a chart and removes one if there are too many points
function addChartPoint(chart_id, point_value){
	var target_graph = charts[chart_id];
	
	if(target_graph != undefined){
		console.log(target_graph);
		if(target_graph.datasets[0].points.length > max_points){
			target_graph.removeData();
		}
		target_graph.addData([point_value], "");
	}
}