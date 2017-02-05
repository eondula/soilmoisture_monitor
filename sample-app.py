import ibmiotf.application
try:
  options = {
    "org": "vy8sg5",
    "id": "Sample",
    "auth-method": "apikey",
    "auth-key": "a-vy8sg5-6jkztbztcy",
    "auth-token": "joadwehNRpIM0AhOoH",
    "clean-session": "true"
  }
  client = ibmiotf.application.Client(options)
except ibmiotf.ConnectionException  as e:
    print "Unable to connect to Watson IoT"

client.connect()
client.subscribeToDeviceEvents(deviceType="intellisoft-sample", deviceId="intellisoftsample1",event="status")
