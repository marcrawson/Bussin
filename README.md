# Bussin'

### Real-time bus monitoring and forecasting

Introducing the solution for frustrated commuters everywhere: Bussin', the app that predicts the arrival times of BC Transit buses using machine learning. Say goodbye to the uncertainty of public transportation and welcome a stress-free commute. Whether you're running late for work or trying to avoid standing in the rain, Bussin' has you covered with real-time updates and accurate predictions days in advance. Experience the future of transportation.

### Machine-learning pseudocode

    Server obtains historical data through APIs and gtfs-realtime data, processes it, and saves it.

    Python script accepts training data.
    
    Python cleans data set.
    
    Algorithm trains neural network.
    
    Algorithm calculates if future buses are likely to be on-time or late.

### Data sources:
- [Weather](Weather)
  - Temperature
  - Precipitation
  - Visibility
- [Date](Date)
  - Month
  - Day-of-week
  - School day
  - Time-of-day
- [Bus](Bus)
  - Route number
  - Stop-id

Weather

Date

Bus
