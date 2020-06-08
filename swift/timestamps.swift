// getting a timestamp string
// https://stackoverflow.com/questions/37126257/swift-full-date-with-milliseconds
let d = Date()
let df = DateFormatter()
df.dateFormat = "y-MM-dd H:m:ss.SSSS"

df.string(from: d) // -> "2016-11-17 17:51:15.1720"
