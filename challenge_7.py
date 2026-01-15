#Log Message Analyzer

#Message must not be empty
#Must contain the word "error" (case-insensitive)
#Count how many times "error" appears
#Message length must be < 200
#Output summary using f-string

log = "Error occurred. ERROR while processing. minor error detected."
log = log.strip()
valid = True

#Message must not be empty
if log =="":
    print("Message must not be empty")
    valid = False

#Must contain the word "error" (case-insensitive)
if not "error" in log.lower():
    print("Must contain the word \"error\" (case-insensitive)")
    valid = False

#Count how many times "error" appears
err_count = log.lower().count("error")

#Message length must be < 200
if not len(log) <200:
    print("Message length must be < 200")
    valid = False

 #Output summary using f-string   
if valid:
    print(f"Error found {err_count} times in log")