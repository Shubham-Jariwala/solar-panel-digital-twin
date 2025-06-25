# Solar Panel Digital Twin

This project simulates the behavior of a solar panel and provides a dashboard for visualizing the data. The simulation calculates energy output based on sunlight exposure and efficiency, while the dashboard allows users to interact with and visualize the simulation results.

## Project Structure

```
solar-panel-digital-twin
├── src
│   ├── simulation
│   │   ├── solar_panel.py       # Contains the SolarPanel class for simulation
│   │   └── interface.py          # Provides an interface for interacting with the SolarPanel class
│   ├── dashboard
│   │   ├── app.py                # Sets up the web application for the dashboard
│   │   └── plots.py              # Contains functions for generating visualizations
│   ├── data
│   │   └── sample_data.csv       # Sample data for testing the simulation and dashboard
│   └── utils
│       └── helpers.py            # Utility functions for data processing and calculations
├── requirements.txt               # Lists the dependencies required for the project
└── README.md                      # Documentation for the project
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/Shubham-Jariwala/solar-panel-digital-twin.git
   cd solar-panel-digital-twin
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Running the Simulation

To start the simulation, run the following command:
```
python src/simulation/interface.py
```

### Accessing the Dashboard

To view the dashboard, run:
```
python src/dashboard/app.py
```
Then open your web browser and navigate to `http://localhost:5000` (or the specified port).

### Implementation

<p align="center">
  <img src="![GIF-2025-06-13-13-26-56](https://github.com/user-attachments/assets/cfce0203-2fed-4eab-919e-4310bda59ffb)" width="600" />
</p>

## Features

- **Simulation**: The SolarPanel class simulates energy output based on sunlight exposure and efficiency.
- **Dashboard**: A web-based interface for visualizing energy output and efficiency over time.
- **Data Visualization**: Includes various plots to analyze the performance of the solar panel.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.
