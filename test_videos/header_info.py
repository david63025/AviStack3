import subprocess

def header_info(fname):
	'''(str)-->dictionary
	gets filename and retrieves header information using the 
	program 'mediainfo', and
	parses it into a dictionary named header.  header is returned
	'''
	p = subprocess.Popen(["mediainfo",  fname], stdout=subprocess.PIPE)
	output, err = p.communicate()
	header={}
							#print output
	x1=output.find(chr(10)) #skip general
							#print output[0:x1]
	
	x2=output.find(chr(10),x1+1)		#print output[x1+1:x2]
										#key=output[x1+1:x2].find(':') #key is 41
										#print key
	string1=output[x1+1:x1+41].strip()	#print string1
	string2=output[x1+43:x2].strip()	#print string2
	header={string1:string2}			#print header
	
	x3=output.find(chr(10),x2+1)
	string1=output[x2+1:x2+41].strip() 	#print string1
	string2=output[x2+43:x3].strip()	#print string2
	header[string1]=string2				#print header
	
	
	x4=output.find(chr(10),x3+1)		#print output[x3+1:x4]
	string1=output[x3+1:x3+41].strip()	#print string1
	string2=output[x3+43:x4].strip()	#print string2
	header[string1]=string2				#print header
	
	
	x5=output.find(chr(10),x4+1)		#print output[x4+1:x5]
	string1=output[x4+1:x4+41].strip()	#print string1
	string2=output[x4+43:x5].strip()	#print string2
	header[string1]=string2				#print header
	
	
	x6=output.find(chr(10),x5+1)		#print output[x5+1:x6]
	string1=output[x5+1:x5+41].strip()	#print string1
	string2=output[x5+43:x6].strip()	#print string2
	header[string1]=string2				#print header
	
	
	
	x7=output.find(chr(10),x6+1)		#print output[x6+1:x7]
	string1=output[x6+1:x6+41].strip()	#print string1
	string2=output[x6+43:x7].strip()	#print string2
	header[string1]=string2				#print header
	
	
	x8=output.find(chr(10),x7+1)		#print output[x7+1:x8]
	string1=output[x7+1:x7+41].strip()	#print string1
	string2=output[x7+43:x8].strip()	#print string2
	header[string1]=string2				#print header
	
	
	
	x9=output.find(chr(10),x8+1)		#print output[x8+1:x9]
	string1=output[x8+1:x8+41].strip()	#print string1
	string2=output[x8+43:x9].strip()	#print string2
	header[string1]=string2				#print header
	
	
	x10=output.find(chr(10),x9+1)		#print output[x9+1:x10]
	string1=output[x9+1:x9+41].strip()	#print string1
	string2=output[x9+43:x10].strip()	#print string2
	header[string1]=string2				#print header
		
	x11=output.find(chr(10),x10+1)  	#blank line
	#print output[x10+1:x11]
	
	
	x12=output.find(chr(10),x11+1) 			#skip video
	#print output[x11+1:x12]
	
	x13=output.find(chr(10),x12+1)			#print output[x12+1:x13]
	string1=output[x12+1:x12+41].strip()	#print string1
	string2=output[x12+43:x13].strip()		#print string2
	header[string1]=string2					#print header
	
	
	x14=output.find(chr(10),x13+1)			#print output[x13+1:x14]
	string1=output[x13+1:x13+41].strip()	#print string1
	string2=output[x13+43:x14].strip()		#print string2
	header[string1]=string2					#print header
	
	x15=output.find(chr(10),x14+1)			#print output[x14+1:x15]
	string1=output[x14+1:x14+41].strip()	#print string1
	string2=output[x14+43:x15].strip()		#print string2
	header[string1]=string2					#print header
	
	x16=output.find(chr(10),x15+1)			#print output[x15+1:x16]
	string1=output[x15+1:x15+41].strip()	#print string1
	string2=output[x15+43:x16].strip()		#print string2
	header[string1]=string2					#print header
	
	x17=output.find(chr(10),x16+1)			#print output[x16+1:x17]
	string1=output[x16+1:x16+41].strip()	#print string1
	string2=output[x16+43:x17].strip()		#print string2
	header[string1]=string2					#print header
	
	x18=output.find(chr(10),x17+1)			#print output[x17+1:x18]
	string1=output[x17+1:x17+41].strip()	#print string1
	string2=output[x17+43:x18].strip()		#print string2
	header[string1]=string2					#print header
	
	x19=output.find(chr(10),x18+1)			#print output[x18+1:x19]
	string1=output[x18+1:x18+41].strip()	#print string1
	string2=output[x18+43:x19].strip()		#print string2
	header[string1]=string2					#print header
	
	x20=output.find(chr(10),x19+1)			#print output[x19+1:x20]
	string1=output[x19+1:x19+41].strip()	#print string1
	string2=output[x19+43:x20].strip()		#print string2
	header[string1]=string2					#print header
	
	x21=output.find(chr(10),x20+1)			#print output[x20+1:x21]
	string1=output[x20+1:x20+41].strip()	#print string1
	string2=output[x20+43:x21].strip()		#print string2
	header[string1]=string2					#print header
	
	x22=output.find(chr(10),x21+1)			#print output[x21+1:x22]
	string1=output[x21+1:x21+41].strip()	#print string1
	string2=output[x21+43:x22].strip()		#print string2
	header[string1]=string2					#print header
	
	x23=output.find(chr(10),x22+1)			#print output[x22+1:x23]
	string1=output[x22+1:x22+41].strip()	#print string1
	string2=output[x22+43:x23].strip()		#print string2
	header[string1]=string2					#print header
	
	x24=output.find(chr(10),x23+1)			#print output[x23+1:x24]
	string1=output[x23+1:x23+41].strip()	#print string1
	string2=output[x23+43:x24].strip()		#print string2
	header[string1]=string2					#print header
	
	x25=output.find(chr(10),x24+1)			#print output[x24+1:x25]
	string1=output[x24+1:x24+41].strip()	#print string1
	string2=output[x24+43:x25].strip()		#print string2
	header[string1]=string2					#print header
	
	x26=output.find(chr(10),x25+1)			#print output[x25+1:x26]
	string1=output[x25+1:x25+41].strip()	#print string1
	string2=output[x25+43:x26].strip()		#print string2
	header[string1]=string2					#print header
	
	
	x27=output.find(chr(10),x26+1)			#print output[x26+1:x27]
	string1=output[x26+1:x26+41].strip()	#print string1
	string2=output[x26+43:x27].strip()		#print string2
	header[string1]=string2					#print header
	
	return header
	
	
	
	
	
	
	
	
	
if __name__ == "__main__":
	h_info=header_info('m02.avi')
	print h_info
		
	
	
