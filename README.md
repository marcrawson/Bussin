# Bussin'

### Real-time bus monitering and forecasting

Introducing Bussin'

Introducing the ultimate solution for frustrated commuters everywhere: BusTracker, the app that predicts the arrival time of city buses using state-of-the-art machine learning algorithms! Say goodbye to the uncertainty of public transportation and hello to a stress-free commute. Whether you're running late for work or just trying to avoid standing in the rain, BusTracker has got you covered with real-time updates and accurate predictions. Download now and experience the future of transportation!

### Machine-learning pseudocode

    Server obtains data through APIs and gtfs-realtime data, processes it, and saves it into a .csv file.

    Python script accepts .csv file training data.
    
    Python cleans data set for use in training.
    
    Algorithm trains neural network, calculating synaptic weights.
    
    Synaptic weights are then used to calculate if future buses are likely to be on-time or late.

### Data sources include:
- Weather
  - Temperature
  - Precipitation
  - Visibility
- Date
  - Month
  - Day-of-week
  - School day
- Time
  - Time-of-day
- Bus factors
  - Route number
  - Stop-id
