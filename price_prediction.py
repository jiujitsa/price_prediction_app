from pydantic import BaseModel
import numpy as np
feature_names = ['CPSCII Name=Acoustic Control Components',
       'CPSCII Name=Air Cleaner',
       'CPSCII Name=Air Handling/Body Ventilation Subsystem',
       'CPSCII Name=Applied Parts - (IP)',
       'CPSCII Name=Auxiliary Water Pump', 'CPSCII Name=Badging',
       'CPSCII Name=Battery Cables',
       'CPSCII Name=Beam Rear Axle Assembly',
       'CPSCII Name=Body And Rear End Wiring',
       'CPSCII Name=Body Dash and Cowl', 'CPSCII Name=Body Side',
       'CPSCII Name=Brake Controls', 'CPSCII Name=Brake Lines and Hoses',
       'CPSCII Name=CHMSL (Center High Mount Stop Light)',
       'CPSCII Name=Cab Back & Ring Frame',
       'CPSCII Name=Clutch Actuation Assembly',
       'CPSCII Name=Cross-Car Beam (IP)',
       'CPSCII Name=Drive Belts/Pulleys and Component Mounting Bracketry',
       'CPSCII Name=EDS Components & Fasteners',
       'CPSCII Name=Emission Control Components',
       'CPSCII Name=Emissions Additive Storage, Supply and Conditioning',
       'CPSCII Name=Engine Bay Fuse Box / Passive',
       'CPSCII Name=Engine Compartment Trim / E-Box',
       'CPSCII Name=Exterior Mirrors',
       'CPSCII Name=Front Bumper Skin and Foams',
       'CPSCII Name=Front Door BIW', 'CPSCII Name=Front Door Trim Panel',
       'CPSCII Name=Front Fenders', 'CPSCII Name=Front Floor',
       'CPSCII Name=Front Floor Console Main Moulding',
       'CPSCII Name=Front Foundation Brakes Subsystem',
       'CPSCII Name=Front Seat Frames',
       'CPSCII Name=Front Side Door Dynamic Weatherstrip',
       'CPSCII Name=Front Side Door Glass',
       'CPSCII Name=Front Stabilizer (Anti-Roll) Bar',
       'CPSCII Name=Front Structure', 'CPSCII Name=Front Strut / Damper',
       'CPSCII Name=Front Sub-Frame',
       'CPSCII Name=Front Suspension Knuckle Assembly',
       'CPSCII Name=Front Wheel Arch Liners',
       'CPSCII Name=Fuel Distribution',
       'CPSCII Name=Fuel Filler (Refueling)',
       'CPSCII Name=Fuel Filler and Flap',
       'CPSCII Name=Fuel Tank Assembly', 'CPSCII Name=Headlamp Cluster',
       'CPSCII Name=Headliner Assembly',
       'CPSCII Name=High Pressure Ducts', 'CPSCII Name=Hood BIW Panel',
       'CPSCII Name=Hose Set - Coolant (includes Expansion Tank)',
       'CPSCII Name=Infotainment Antennas and Cables',
       'CPSCII Name=Inner Handles and Actuation',
       'CPSCII Name=Intercooler For Pressure-Charged Engines',
       'CPSCII Name=Interior Mirror',
       'CPSCII Name=Load Compartment Floor Trim',
       'CPSCII Name=Lower Exterior Finishers',
       'CPSCII Name=Manual Gearchange Mechanism',
       'CPSCII Name=NS Powertrain Mounting System',
       'CPSCII Name=NVH Pads',
       'CPSCII Name=Noise Insulation, Engine Bay and Underfloor',
       'CPSCII Name=One Piece Body Structure',
       'CPSCII Name=Overhead Console',
       'CPSCII Name=Parking Brake Cables and Attaching Components',
       'CPSCII Name=Parking Brake Controls', 'CPSCII Name=Pedals',
       'CPSCII Name=Pillar Trim Lower', 'CPSCII Name=Pillar Trim Upper',
       'CPSCII Name=Powertrain Control Modules: Mounting Hardware',
       'CPSCII Name=Powertrain Control: Sensors and Actuators',
       'CPSCII Name=Powertrain Mount - Pendulum System',
       'CPSCII Name=Rain Sensor/Daylight Sensor/Sunload Sensor',
       'CPSCII Name=Rear Bumper Skin and Foams',
       'CPSCII Name=Rear Closure BIW Panel',
       'CPSCII Name=Rear Closure Dynamic Weatherstrip',
       'CPSCII Name=Rear Closure Finishers',
       'CPSCII Name=Rear Closure Hinges',
       'CPSCII Name=Rear Closure Interior Trim Panel',
       'CPSCII Name=Rear Closure Latches',
       'CPSCII Name=Rear Closure Support & Checks',
       'CPSCII Name=Rear Combination Lamp', 'CPSCII Name=Rear Door BIW',
       'CPSCII Name=Rear Floor', 'CPSCII Name=Rear Non-Driven Axles',
       'CPSCII Name=Rear Road Spring',
       'CPSCII Name=Rear Side Door Dynamic Weatherstrip',
       'CPSCII Name=Rear Stabilizer (Anti-Roll) Bar',
       'CPSCII Name=Rear Strut / Damper',
       'CPSCII Name=Rear Suspension Knuckle Assembly',
       'CPSCII Name=Rear Suspension Links/Arms Upper & Lower',
       'CPSCII Name=Rear Wheel Arch Liners',
       'CPSCII Name=Rearward Propeller Shaft',
       'CPSCII Name=Restraint Electronics',
       'CPSCII Name=Road Wheel and Tire Assembly',
       'CPSCII Name=Roof and Cross-Member',
       'CPSCII Name=Seat Belt Assembly Front Row',
       'CPSCII Name=Servo Equipment', 'CPSCII Name=Side Door Latches',
       'CPSCII Name=Side Doors Hinges and Checks',
       'CPSCII Name=Sliding Door Mechanism - Power or Manual',
       'CPSCII Name=Sliding Door Module and Electronics',
       'CPSCII Name=Spare Wheel and Tire Assembly',
       'CPSCII Name=Starter Motor', 'CPSCII Name=Static Sealing',
       'CPSCII Name=Steering Column and Shroud Mounted - Switches and Clockspring',
       'CPSCII Name=Steering Gear',
       'CPSCII Name=Supplemental Front Lamps',
       'CPSCII Name=Switch Pack - Front Door',
       'CPSCII Name=Switches - Overhead',
       'CPSCII Name=Under Engine Closures or Rock Shields',
       'CPSCII Name=Underfloor Closures', 'CPSCII Name=Windshield',
       'CPSCII Name=Wiper Assembly Front', 'online_price']
       
class Part(BaseModel):
    

    part_dict: dict
    
    

    part_dict = { parameter : 0 for parameter in feature_names }