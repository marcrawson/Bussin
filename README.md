# Bussin'

### Real-time bus monitering and forecasting

Introducing solution for frustrated commuters everywhere: Bussin', the app that predicts the arrival times of BC Transit city buses using machine learning. Say goodbye to the uncertainty of public transportation and hello to a stress-free commute. Whether you're running late for work or just trying to avoid standing in the rain, Bussin' has got you covered with real-time updates and accurate predictions, even days in advance. Use Bussin' and experience the future of transportation.

### Machine-learning pseudocode

    Server obtains data through APIs and gtfs-realtime data, processes it, and saves it into a .csv file.

    Python script accepts .csv file training data.
    
    Python cleans data set for use in training.
    
    Algorithm trains neural network, calculating synaptic weights.
    
    Synaptic weights are then used to calculate if future buses are likely to be on-time or late.

### Data sources:
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

### Creators
**Luca Tozzini**  
github.com/LucaTozzini/

**Marc Rawson**  
github.com/marcrawson/
