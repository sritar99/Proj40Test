import aiml

kernel=aiml.Kernel()

kernel.learn("std-startup.xml")
kernel.respond("load aiml b")


while True:
	inp=input("Ask me anything:   ")
	response=kernel.respond(inp)
	print("Bot>"+response)