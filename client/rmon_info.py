import psutil

network = psutil.net_io_counters
memory = psutil.virtual_memory
cpu_perc = psutil.cpu_percent


#HELPER FUNCTIONS
def byteResolution(bytes, factor):
	return round(bytes/pow(1024, factor),2)


def bytesToKilo(bytes):
	return byteResolution(bytes, 1)
	
	
def bytesToMega(bytes):
	return byteResolution(bytes, 2)
	

def bytesToGiga(bytes):
	return byteResolution(bytes, 3)

	


#START CPU INFORMATION
def packCPUInfo():
	return {"usage": cpu_perc()}

	
#START MEMORY INFORMATION
def packMemoryInfo():
	return {"total": bytesToGiga(memory().total), "used": bytesToGiga(memory().used)}


#START NETWORK INFORMATION
def packNetworkInfo():
	return {"bytes_sent": bytesToGiga(network().bytes_sent), "bytes_received": bytesToGiga(network().bytes_recv), "packets_sent": network().packets_sent, "packets_received": network().packets_recv}
	
	
#TOP LEVEL FUNCTION
def packAllInfo():
	return {"cpu": packCPUInfo(), "memory": packMemoryInfo(), "network": packNetworkInfo()}
