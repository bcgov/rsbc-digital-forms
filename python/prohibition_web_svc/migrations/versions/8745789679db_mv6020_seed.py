"""mv6020-seed

Revision ID: 8745789679db
Revises: 2c51e711695d
Create Date: 2025-07-09 15:01:12.267486

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8745789679db'
down_revision = '2c51e711695d'
branch_labels = None
depends_on = None


def upgrade():
    # road_class
    op.execute('''
        INSERT INTO "TAR"."road_class" (code, description) VALUES
        ('11', 'One Lane Undivided'),
        ('12', 'One Lane Divided'),
        ('13', 'One Lane Ramp'),
        ('21', 'Two Lane Undivided'),
        ('22', 'Two Lane Divided'),
        ('23', 'Two Lane Ramp'),
        ('31', 'Three Lane Undivided'),
        ('32', 'Three Lane Divided'),
        ('33', 'Three Lane Ramp'),
        ('41', 'Four Lane Undivided'),
        ('42', 'Four Lane Divided'),
        ('43', 'Four Lane Ramp'),
        ('51', 'Five Lane Undivided'),
        ('52', 'Five Lane Divided'),
        ('53', 'Five Lane Ramp'),
        ('61', 'Six Lane Undivided'),
        ('62', 'Six Lane Divided'),
        ('63', 'Six Lane Ramp'),
        ('71', 'Seven Lane Undivided'),
        ('72', 'Seven Lane Divided'),
        ('73', 'Seven Lane Ramp'),
        ('98', 'Parking Lot or Off Highway'),
        ('99', 'Other'),
        ('00', 'Unknown');
    ''')

    # traffic_flow
    op.execute('''
        INSERT INTO "TAR"."traffic_flow" (code, description) VALUES
        ('01', 'One Way'),
        ('02', 'Two Way'),
        ('99', 'Other'),
        ('00', 'Unknown');
    ''')

    # collision_location
    op.execute('''
        INSERT INTO "TAR"."collision_location" (code, description) VALUES
        ('01', 'At Intersection'),
        ('02', 'Between Intersection/Exchanges'),
        ('03', 'Intersection of Road and Driveway or Alley'),
        ('04', 'Bridge'),
        ('05', 'Ferry or Dock'),
        ('06', 'Tunnel'),
        ('07', 'Exit Deceleration Lane'),
        ('08', 'Exit Ramp'),
        ('09', 'Exit Intersection'),
        ('10', 'Entrance Acceleration Lane'),
        ('11', 'Entrance Ramp'),
        ('12', 'Entrance Intersection'),
        ('13', 'Off Highway (incl. private land / driveways)'),
        ('14', 'Parking Lot Single / Multilevel'),
        ('15', 'RR Crossing'),
        ('16', 'Industrial Road'),
        ('17', 'Transit Express Lane'),
        ('18', 'Forest Service / Logging Road'),
        ('19', 'Public Driveway'),
        ('99', 'Other'),
        ('00', 'Unknown');
    ''')

    # speed_zone
    op.execute('''
        INSERT INTO "TAR"."speed_zone" (code, description) VALUES
        ('101', 'Posted - 10 km/h'),
        ('102', 'Posted - 20 km/h'),
        ('103', 'Posted - 30 km/h'),
        ('104', 'Posted - 40 km/h'),
        ('105', 'Posted - 50 km/h'),
        ('106', 'Posted - 60 km/h'),
        ('107', 'Posted - 70 km/h'),
        ('108', 'Posted - 80 km/h'),
        ('109', 'Posted - 90 km/h'),
        ('110', 'Posted - 100 km/h'),
        ('111', 'Posted - 110 km/h'),
        ('112', 'Posted - 120 km/h'),
        ('201', 'Advisory - 10 km/h'),
        ('202', 'Advisory - 20 km/h'),
        ('203', 'Advisory - 30 km/h'),
        ('204', 'Advisory - 40 km/h'),
        ('205', 'Advisory - 50 km/h'),
        ('206', 'Advisory - 60 km/h'),
        ('207', 'Advisory - 70 km/h'),
        ('208', 'Advisory - 80 km/h'),
        ('209', 'Advisory - 90 km/h'),
        ('210', 'Advisory - 100 km/h'),
        ('211', 'Advisory - 110 km/h'),
        ('212', 'Advisory - 120 km/h'),
        ('301', 'Special - 10 km/h'),
        ('302', 'Special - 20 km/h'),
        ('303', 'Special - 30 km/h'),
        ('304', 'Special - 40 km/h'),
        ('305', 'Special - 50 km/h'),
        ('306', 'Special - 60 km/h'),
        ('307', 'Special - 70 km/h'),
        ('308', 'Special - 80 km/h'),
        ('309', 'Special - 90 km/h'),
        ('310', 'Special - 100 km/h'),
        ('311', 'Special - 110 km/h'),
        ('312', 'Special - 120 km/h'),
        ('401', 'Not Posted - 10 km/h'),
        ('402', 'Not Posted - 20 km/h'),
        ('403', 'Not Posted - 30 km/h'),
        ('404', 'Not Posted - 40 km/h'),
        ('405', 'Not Posted - 50 km/h'),
        ('406', 'Not Posted - 60 km/h'),
        ('407', 'Not Posted - 70 km/h'),
        ('408', 'Not Posted - 80 km/h'),
        ('409', 'Not Posted - 90 km/h'),
        ('410', 'Not Posted - 100 km/h'),
        ('411', 'Not Posted - 110 km/h'),
        ('412', 'Not Posted - 120 km/h'),
        ('000', 'Unknown');
    ''')

    # land_usage
    op.execute('''
        INSERT INTO "TAR"."land_usage" (code, description) VALUES
        ('01', 'School/Playground'),
        ('02', 'Urban Residential'),
        ('03', 'Apartment Residential'),
        ('04', 'Business/Shopping'),
        ('05', 'Industrial/Manufacturing'),
        ('06', 'Agricultural/Undeveloped'),
        ('07', 'Recreational/Park/Camping'),
        ('08', 'Rural Residential'),
        ('99', 'Other'),
        ('00', 'Unknown');
    ''')

    # road_type
    op.execute('''
        INSERT INTO "TAR"."road_type" (code, description) VALUES
        ('01', 'Asphalt'),
        ('02', 'Gravel'),
        ('03', 'Oiled Gravel'),
        ('04', 'Earth'),
        ('05', 'Concrete'),
        ('06', 'Brick/Stone'),
        ('07', 'Wood'),
        ('99', 'Other'),
        ('00', 'Unknown');
    ''')

    # traffic_control
    op.execute('''
        INSERT INTO "TAR"."traffic_control" (code, description) VALUES
        ('01', 'None'),
        ('02', 'Stop Sign'),
        ('03', 'Yield Sign'),
        ('04', 'Officer / Flagman / School Guard'),
        ('05', 'Railroad Crossing Sign'),
        ('06', 'Lane Use / Turn Control Sign'),
        ('21', 'Traffic Signal - Red'),
        ('22', 'Traffic Signal - Yellow'),
        ('23', 'Traffic Signal - Green'),
        ('31', 'Traffic Signal with Advance Flashers - Red'),
        ('32', 'Traffic Signal with Advance Flashers - Yellow'),
        ('33', 'Traffic Signal with Advance Flashers - Green'),
        ('41', 'Flashing Signal - Red'),
        ('42', 'Flashing Signal - Yellow'),
        ('43', 'Flashing Signal - Green'),
        ('51', 'Lane Use Signal - Red'),
        ('52', 'Lane Use Signal - Yellow'),
        ('53', 'Lane Use Signal - Green'),
        ('99', 'Other'),
        ('00', 'Unknown');
    ''')

    # roadway_character
    op.execute('''
        INSERT INTO "TAR"."roadway_character" (code, description) VALUES
        ('11', 'Straight / Flat'),
        ('12', 'Straight / Some Grade'),
        ('13', 'Straight / Steep Grade'),
        ('14', 'Straight / Hillcrest'),
        ('15', 'Straight / Sag'),
        ('21', 'Single Curve / Flat'),
        ('22', 'Single Curve / Some Grade'),
        ('23', 'Single Curve / Steep Grade'),
        ('24', 'Single Curve / Hillcrest'),
        ('25', 'Single Curve / Sag'),
        ('31', 'Sharp Curve / Flat'),
        ('32', 'Sharp Curve / Some Grade'),
        ('33', 'Sharp Curve / Steep Grade'),
        ('34', 'Sharp Curve / Hillcrest'),
        ('35', 'Sharp Curve / Sag'),
        ('41', 'Switchback / Flat'),
        ('42', 'Switchback / Some Grade'),
        ('43', 'Switchback / Steep Grade'),
        ('44', 'Switchback / Hillcrest'),
        ('45', 'Switchback / Sag'),
        ('51', 'Winding Curves / Flat'),
        ('52', 'Winding Curves / Some Grade'),
        ('53', 'Winding Curves / Steep Grade'),
        ('54', 'Winding Curves / Hillcrest'),
        ('55', 'Winding Curves / Sag'),
        ('61', 'Reverse Curve / Flat'),
        ('62', 'Reverse Curve / Some Grade'),
        ('63', 'Reverse Curve / Steep Grade'),
        ('64', 'Reverse Curve / Hillcrest'),
        ('65', 'Reverse Curve / Sag'),
        ('99', 'Other'),
        ('00', 'Unknown');
    ''')

    # roadway_condition
    op.execute('''
        INSERT INTO "TAR"."roadway_condition" (code, description) VALUES
        ('01', 'Dry'),
        ('02', 'Wet'),
        ('03', 'Muddy'),
        ('04', 'Snow'),
        ('05', 'Slush'),
        ('06', 'Ice'),
        ('99', 'Other'),
        ('00', 'Unknown');
    ''')

    # weather_condition
    op.execute('''
        INSERT INTO "TAR"."weather_condition" (code, description) VALUES
        ('01', 'Clear'),
        ('02', 'Cloudy'),
        ('03', 'Raining'),
        ('04', 'Snowing/Sleet'),
        ('05', 'Hail'),
        ('06', 'Fog'),
        ('07', 'Smog/Smoke'),
        ('08', 'Strong Wind'),
        ('99', 'Other'),
        ('00', 'Unknown');
    ''')

    # lighting_condition
    op.execute('''
        INSERT INTO "TAR"."lighting_condition" (code, description) VALUES
        ('01', 'Daylight'),
        ('02', 'Dawn'),
        ('03', 'Dusk'),
        ('04', 'Dark / Full Illumination'),
        ('05', 'Dark / No Illumination'),
        ('06', 'Dark / Some Illumination'),
        ('99', 'Other'),
        ('00', 'Unknown');
    ''')

    # type_of_collision
    op.execute('''
        INSERT INTO "TAR"."type_of_collision" (code, description, type) VALUES
        ('01', 'Other Motor Vehicle', 'Moving objects'),
        ('02', 'Motorcycle', 'Moving objects'),
        ('03', 'Pedestrian', 'Moving objects'),
        ('04', 'Bicyclist', 'Moving objects'),
        ('05', 'Animal', 'Moving objects'),
        ('06', 'Railroad Train', 'Moving objects'),
        ('07', 'Street Car / Trolley Coach', 'Moving objects'),
        ('08', 'All-Terrain Vehicle', 'Moving objects'),
        ('09', 'Moped (under 50cc)', 'Moving objects'),
        ('20', 'Light Support Pole', 'Fixed objects'),
        ('21', 'Utility Support Pole', 'Fixed objects'),
        ('22', 'Guard Rail / Traffic Barrier', 'Fixed objects'),
        ('23', 'Crash Cushion / Impact Attenuator', 'Fixed objects'),
        ('24', 'Sign Post', 'Fixed objects'),
        ('25', 'Tree', 'Fixed objects'),
        ('26', 'Building Wall', 'Fixed objects'),
        ('27', 'Curbing', 'Fixed objects'),
        ('28', 'Fence', 'Fixed objects'),
        ('29', 'Bridge Deck or Parapet', 'Fixed objects'),
        ('30', 'Raised Traffic Island', 'Fixed objects'),
        ('31', 'Snow Bank/Drift', 'Fixed objects'),
        ('32', 'Rock Face', 'Fixed objects'),
        ('33', 'Ditch', 'Fixed objects'),
        ('34', 'Culvert', 'Fixed objects'),
        ('35', 'Fire Hydrant', 'Fixed objects'),
        ('36', 'Rocks or Debris', 'Fixed objects'),
        ('40', 'Over Turned', 'Non collision'),
        ('41', 'Fire/Explosion', 'Non collision'),
        ('42', 'Submersion (Lake, River, Slough)', 'Non collision'),
        ('43', 'Ran Off / Left Roadway', 'Non collision'),
        ('44', 'Runway or Grade', 'Non collision'),
        ('99', 'Other', 'Non collision'),
        ('00', 'Unknown', 'Unknown');
    ''')

    # location_of_first_contact
    op.execute('''
        INSERT INTO "TAR"."location_of_first_contact" (code, description) VALUES
        ('01', 'On Roadway'),
        ('02', 'Off Roadway'),
        ('00', 'Unknown');
    ''')

    # primary_collision_occurrence
    op.execute('''
        INSERT INTO "TAR"."primary_collision_occurrence" (code, description) VALUES
        ('01', 'Rear End'),
        ('02', 'Head On'),
        ('03', 'Side Swipe - opposite direction'),
        ('04', 'Backing'),
        ('05', 'Intersection 90 degrees'),
        ('06', 'Overtaking'),
        ('07', 'Right Turn (cutoff)'),
        ('08', 'Right Turn (head on)'),
        ('09', 'Right Turn (travelling same direction)'),
        ('10', 'Right Turn (travelling opposite direction)'),
        ('11', 'Left Turn (head on)'),
        ('12', 'Left Turn (cutoff)'),
        ('13', 'Left Turn (traveling same direction)'),
        ('14', 'Left Turn (turn in front of)'),
        ('15', 'Off Road Right'),
        ('16', 'Off Road Left'),
        ('17', 'One Way Street'),
        ('99', 'Other, Explain in Comments'),
        ('00', 'Unknown');
    ''')

    # pedestrian_location
    op.execute('''
        INSERT INTO "TAR"."pedestrian_location" (code, description) VALUES
        ('01', 'At Intersection'),
        ('02', 'Not at intersection'),
        ('00', 'Unknown'),
        ('98', 'No Pedestrian Involved');
    ''')

    # pedestrian_action
    op.execute('''
        INSERT INTO "TAR"."pedestrian_action" (code, description) VALUES
        ('01', 'Crossing with Signal'),
        ('02', 'Crossing Against Signal'),
        ('03', 'Crossing, No Signal, Marked Crosswalk'),
        ('04', 'Crossing, No Signal, No Marked Crosswalk'),
        ('05', 'Walking along Highway with Traffic'),
        ('06', 'Walking along Highway against Traffic'),
        ('07', 'Emerging from Front/Behind Parked Vehicle'),
        ('08', 'Child Getting on/off School Bus/Vehicle'),
        ('09', 'Adult Getting on/off a Vehicle'),
        ('10', 'Pushing/Working on a Vehicle'),
        ('11', 'Working in Roadway'),
        ('12', 'Playing in Roadway'),
        ('13', 'Standing/Walking on Sidewalk'),
        ('99', 'Other (explain in Comments)'),
        ('00', 'Unknown'),
        ('98', 'No Pedestrian Involved');
    ''')

    # entity_type
    op.execute('''
        INSERT INTO "TAR"."entity_type" (code, description) VALUES
        ('V', 'Vehicle'),
        ('C', 'Cyclist'),
        ('P', 'Pedestrian'),
        ('O', 'Other');
    ''')

    # contributing_factors
    op.execute('''
        INSERT INTO "TAR"."contributing_factors" (code, description, type) VALUES
        ('00', 'Unknown', 'Human Conditions'),
        ('16', 'Extreme fatigue', 'Human Conditions'),
        ('19', 'Fell asleep', 'Human Conditions'),
        ('22', 'Illness (*police comments)', 'Human Conditions'),
        ('23', 'Sudden loss of consciousness', 'Human Conditions'),
        ('26', 'Pre-existing physical disability', 'Human Conditions'),
        ('80', 'Ability impaired by alcohol', 'Human Conditions'),
        ('81', 'Alcohol suspected', 'Human Conditions'),
        ('82', 'Ability impaired by drugs', 'Human Conditions'),
        ('83', 'Drugs suspected', 'Human Conditions'),
        ('84', 'Ability impaired by medication', 'Human Conditions'),
        ('85', 'Driver inattentive', 'Human Conditions'),
        ('86', 'Driver internal/external distraction', 'Human Conditions'),
        ('87', 'Deceased prior to collision', 'Human Conditions'),
        ('11', 'Backing unsafely', 'Human Action'),
        ('12', 'Cutting in', 'Human Action'),
        ('17', 'Failing to signal', 'Human Action'),
        ('18', 'Failing to yield right-of-way', 'Human Action'),
        ('20', 'Following too closely', 'Human Action'),
        ('21', 'Improper passing', 'Human Action'),
        ('24', 'Driving on wrong side of road', 'Human Action'),
        ('25', 'Pedestrian error/confusion', 'Human Action'),
        ('29', 'Ignoring traffic control device', 'Human Action'),
        ('30', 'Improper turning', 'Human Action'),
        ('32', 'Ignoring officer/flagman/guard', 'Human Action'),
        ('33', 'Avoid vehicle/pedestrian/cycle', 'Human Action'),
        ('34', 'Use of communication/video equipment', 'Human Action'),
        ('35', 'Exceeding speed limit', 'Human Action'),
        ('36', 'Excessive speed over 40 km hour', 'Human Action'),
        ('37', 'Driving too fast for conditions', 'Human Action'),
        ('38', 'Failure to secure stopped vehicle', 'Human Action'),
        ('39', 'Driver error/confusion', 'Human Action'),
        ('40', 'Accelerator defective', 'Vehicle Condition'),
        ('41', 'Brakes defective', 'Vehicle Condition'),
        ('42', 'Headlights defective / out', 'Vehicle Condition'),
        ('43', 'Brake lights out', 'Vehicle Condition'),
        ('44', 'Turn signals defective', 'Vehicle Condition'),
        ('45', 'Oversize vehicle', 'Vehicle Condition'),
        ('46', 'Steering failure', 'Vehicle Condition'),
        ('47', 'Tire failure / inadequate', 'Vehicle Condition'),
        ('48', 'Tow hitch failure', 'Vehicle Condition'),
        ('49', 'Driverless vehicle', 'Vehicle Condition'),
        ('50', 'Windshield defective', 'Vehicle Condition'),
        ('51', 'Engine failure', 'Vehicle Condition'),
        ('52', 'Suspension defect', 'Vehicle Condition'),
        ('54', 'Insecure load', 'Vehicle Condition'),
        ('55', 'Dangerous goods', 'Vehicle Condition'),
        ('56', 'Trailer brakes out of adjustment/inoperative', 'Vehicle Condition'),
        ('59', 'Windows obstructed', 'Vehicle Condition'),
        ('60', 'Illegal vehicle modifications', 'Vehicle Condition'),
        ('57', 'Road condition (ice,snow,slush,water)', 'Environmental Condition'),
        ('58', 'Site line obstruction', 'Environmental Condition'),
        ('61', 'Glare-artificial', 'Environmental Condition'),
        ('62', 'Glare-sunlight', 'Environmental Condition'),
        ('63', 'Obstruction/debris on road', 'Environmental Condition'),
        ('64', 'Roadway surface defects', 'Environmental Condition'),
        ('66', 'Weather (fog,sleet,rain,snow)', 'Environmental Condition'),
        ('68', 'Previous traffic accident', 'Environmental Condition'),
        ('70', 'Domestic animal', 'Environmental Condition'),
        ('71', 'Wild animal', 'Environmental Condition'),
        ('72', 'Insufficient worksite/construction traffic control', 'Environmental Condition'),
        ('73', 'Road/intersection design', 'Environmental Condition'),
        ('74', 'Roadside hazard', 'Environmental Condition'),
        ('75', 'Defective/inoperative traffic control device', 'Environmental Condition'),
        ('98', 'Not applicable', 'Other'),
        ('99', 'Other (*see police comments)', 'Other'),
        ('10', 'Alcohol Involvement', 'Other'),
        ('13', 'Driving without due care', 'Other'),
        ('14', 'Driver inexperience', 'Other'),
        ('15', 'Drugs (illegal)', 'Other'),
        ('27', 'Prescribed medication', 'Other'),
        ('28', 'Attempted suicide(confirmed)', 'Other'),
        ('31', 'Unsafe speed', 'Other'),
        ('53', 'Restraint system', 'Other'),
        ('65', 'Visibility impaired', 'Other'),
        ('67', 'Road maintenance/construction', 'Other');
    ''')

    # damage_location
    op.execute('''
        INSERT INTO "TAR"."damage_location" (code, description) VALUES
        ('00', 'Unknown'),
        ('01', 'Front end'),
        ('02', 'Windshield'),
        ('03', 'Front left corner'),
        ('04', 'Front right corner'),
        ('05', 'Rear end'),
        ('06', 'Rear left corner'),
        ('07', 'Rear right corner'),
        ('08', 'Left side'),
        ('09', 'Right side'),
        ('10', 'Left front quarter'),
        ('11', 'Right front quarter'),
        ('12', 'Left rear quarter'),
        ('13', 'Right rear quarter'),
        ('14', 'Tires'),
        ('15', 'Left side & top'),
        ('16', 'Right side & top'),
        ('17', 'Front end / rear end'),
        ('18', 'Front end / left side'),
        ('19', 'Front end / right side'),
        ('20', 'Rear end / left side'),
        ('21', 'Rear end / right side'),
        ('22', 'Right side / left side'),
        ('23', 'Front left / rear right quarter'),
        ('24', 'Front right / rear left quarter'),
        ('25', 'Roof'),
        ('26', 'Undercarriage'),
        ('27', 'Whole vehicle damage'),
        ('98', 'Not applicable'),
        ('99', 'Other');
    ''')

    # damage_severity
    op.execute('''
        INSERT INTO "TAR"."damage_severity" (code, description) VALUES
        ('00', 'Unknown'),
        ('01', 'No damage (none visible)'),
        ('02', 'Light damage (conspicuous but superficial scratches)'),
        ('03', 'Moderate damage (large dents and/or unsafe condition)'),
        ('04', 'Severe damage (major structural repairs needed)'),
        ('05', 'Demolished (repair impractical)'),
        ('98', 'Not applicable'),
        ('99', 'Other');
    ''')

    # pre_collision_action
    op.execute('''
        INSERT INTO "TAR"."pre_collision_action" (code, description) VALUES
        ('00', 'Unknown'),
        ('01', 'Going straight ahead'),
        ('02', 'Making a right turn'),
        ('03', 'Making a left turn'),
        ('04', 'Making “U” turn'),
        ('05', 'Starting from parked position'),
        ('06', 'Starting in traffic'),
        ('07', 'Slowing or stopping'),
        ('08', 'Stopped in traffic'),
        ('09', 'Entered parking position'),
        ('10', 'Parked legally'),
        ('11', 'Parked illegally'),
        ('12', 'Avoiding object on road'),
        ('13', 'Changing lanes'),
        ('14', 'Overtaking'),
        ('15', 'Merging'),
        ('16', 'Backing'),
        ('17', 'Skidding'),
        ('18', 'Swerving'),
        ('19', 'Spinning'),
        ('20', 'Jack-knifing'),
        ('21', 'Yaw'),
        ('98', 'Not applicable'),
        ('99', 'Other');
    ''')

    # vehicle_type
    op.execute('''
        INSERT INTO "TAR"."vehicle_type" (code, description) VALUES
        ('00', 'Unknown'),
        ('01', 'Passenger car only'),
        ('02', 'Passenger car & trailer only'),
        ('05', 'Sport utility vehicle'),
        ('06', 'Sport utility vehicle & trailer'),
        ('07', 'Panel van 4500 kg & under (includes mini vans)'),
        ('08', 'Panel van 4500 kg & under & trailer'),
        ('20', 'Single unit truck / light pickup truck'),
        ('21', 'Single unit truck / heavy'),
        ('30', 'Comb unit truck / light'),
        ('31', 'Comb unit truck / heavy'),
        ('32', 'Comb unit tractor / trailer'),
        ('33', 'Comb unit tractor/trailer & pup'),
        ('34', 'Log truck & pole trailer'),
        ('35', 'Tow truck'),
        ('36', 'Combination unit truck/pull trailer/5th wheel trailer'),
        ('40', 'Bus - school'),
        ('41', 'Bus - local transit'),
        ('42', 'Bus - intercity'),
        ('50', 'Motorcycle'),
        ('51', 'Moped/power bicycle (<50 cc)'),
        ('52', 'Bicycle'),
        ('60', 'Truck / camper'),
        ('61', 'Truck / camper / trailer'),
        ('62', 'Motor home'),
        ('63', 'Motor home / trailer'),
        ('70', 'Trailer only'),
        ('80', 'Snow mobile'),
        ('81', 'Dune buggy'),
        ('82', 'Trail bike'),
        ('83', 'Mini bike'),
        ('84', 'Swamp buggy'),
        ('85', 'Hovercraft'),
        ('86', 'Four wheel drive vehicle'),
        ('87', 'All terrain cycle'),
        ('90', 'Farm tractor, combine, thresher'),
        ('91', 'Road construction (grader, paver, roller)'),
        ('92', 'General construction (backhoe, bulldozer, crawler, digger, excavator, forklift, loader, mower, skidder, trencher)'),
        ('93', 'Mobile home - over width'),
        ('94', 'Mobile crane'),
        ('97', 'Three wheeled vehicle'),
        ('99', 'Other');
    ''')

    # vehicle_use
    op.execute('''
        INSERT INTO "TAR"."vehicle_use" (code, description) VALUES
        ('00', 'Unknown'),
        ('01', 'Parked'),
        ('02', 'Personal'),
        ('03', 'Business / Commercial'),
        ('04', 'Driver Training Facility'),
        ('05', 'Recreational'),
        ('06', 'Emergency'),
        ('07', 'Military'),
        ('08', 'Taxi'),
        ('09', 'Farm Use'),
        ('11', 'Government'),
        ('12', 'Towing / Towed'),
        ('13', 'Stolen'),
        ('21', 'Class 1 – Explosives'),
        ('22', 'Class 2 – Gases'),
        ('23', 'Class 3 – Flammable Liquids'),
        ('24', 'Class 4 – Flammable Solids'),
        ('25', 'Class 5 – Oxidizing Substances'),
        ('26', 'Class 6 – Poison / Infectious'),
        ('27', 'Class 7 – Radioactive Material'),
        ('28', 'Class 8 – Corrosive Substances'),
        ('29', 'Class 9 - Misc. Dangerous Goods'),
        ('98', 'Not Applicable'),
        ('99', 'Other');
    ''')

    # position
    op.execute('''
        INSERT INTO "TAR"."position" (code, description) VALUES
        ('00', 'Unknown'),
        ('01', 'Driver (front left seat)'),
        ('02', 'Front seat center'),
        ('03', 'Front seat right'),
        ('04', 'Back seat left'),
        ('05', 'Back seat center'),
        ('06', 'Back seat right'),
        ('07', 'In cargo area'),
        ('08', 'Riding / hanging outside'),
        ('09', 'Passengers'),
        ('10', 'Passengers'),
        ('11', 'Passengers'),
        ('12', 'Passengers'),
        ('13', 'Passengers'),
        ('14', 'Passengers'),
        ('15', 'Passengers'),
        ('16', 'Passengers'),
        ('17', 'Passengers'),
        ('18', 'Passengers'),
        ('19', 'Passengers'),
        ('20', 'Passengers'),
        ('21', 'Passengers'),
        ('22', 'Passengers'),
        ('23', 'Passengers'),
        ('24', 'Passengers'),
        ('25', 'Passengers'),
        ('26', 'Passengers'),
        ('27', 'Passengers'),
        ('28', 'Passengers'),
        ('29', 'Passengers'),
        ('30', 'Passengers'),
        ('31', 'Passengers'),
        ('32', 'Passengers'),
        ('33', 'Passengers'),
        ('34', 'Passengers'),
        ('35', 'Passengers'),
        ('36', 'Passengers'),
        ('37', 'Passengers'),
        ('38', 'Passengers'),
        ('39', 'Passengers'),
        ('40', 'Passengers'),
        ('41', 'Passengers'),
        ('42', 'Passengers'),
        ('43', 'Passengers'),
        ('44', 'Passengers'),
        ('45', 'Passengers'),
        ('46', 'Passengers'),
        ('47', 'Passengers'),
        ('48', 'Passengers'),
        ('49', 'Passengers'),
        ('50', 'Passengers'),
        ('51', 'Passengers'),
        ('52', 'Passengers'),
        ('53', 'Passengers'),
        ('54', 'Passengers'),
        ('55', 'Passengers'),
        ('56', 'Passengers'),
        ('57', 'Passengers'),
        ('58', 'Passengers'),
        ('59', 'Passengers'),
        ('60', 'Passengers'),
        ('61', 'Passengers'),
        ('62', 'Passengers'),
        ('63', 'Passengers'),
        ('64', 'Passengers'),
        ('65', 'Passengers'),
        ('66', 'Passengers'),
        ('67', 'Passengers'),
        ('68', 'Passengers'),
        ('69', 'Passengers'),
        ('70', 'Passengers'),
        ('71', 'Passengers'),
        ('72', 'Passengers'),
        ('98', 'Not applicable'),
        ('99', 'See Police comments');
    ''')

    # safety_equipment
    op.execute('''
        INSERT INTO "TAR"."safety_equipment" (code, description) VALUES
        ('00', 'Unknown'),
        ('01', 'Position not equipped'),
        ('02', 'No restraint used'),
        ('03', 'Lap belt only'),
        ('04', 'Harness only'),
        ('05', 'Lap & harness'),
        ('06', 'Air bag deployed (no restraint used)'),
        ('07', 'Child restraint used'),
        ('08', 'Helmet'),
        ('09', 'No helmet'),
        ('10', 'Restraint inoperative/broken'),
        ('11', 'Lap & harness & airbag deployed'),
        ('12', 'Lap & harness with no air bag deployed'),
        ('13', 'Misuse of restraint'),
        ('14', 'Misuse of child restraint'),
        ('98', 'Not applicable'),
        ('99', 'Other');
    ''')

    # ejection
    op.execute('''
        INSERT INTO "TAR"."ejection" (code, description) VALUES
        ('00', 'Unknown'),
        ('02', 'Partially ejected'),
        ('01', 'Not ejected'),
        ('03', 'Ejected'),
        ('98', 'Not applicable');
    ''')

    # injury_location
    op.execute('''
        INSERT INTO "TAR"."injury_location" (code, description) VALUES
        ('00', 'Unknown'),
        ('01', 'No injury'),
        ('02', 'Head'),
        ('03', 'Face / nose'),
        ('04', 'Eye'),
        ('05', 'Neck'),
        ('06', 'Chest'),
        ('07', 'Back'),
        ('08', 'Shoulder / upper arm'),
        ('09', 'Elbow / lower arm / hand'),
        ('10', 'Abdomen / pelvis'),
        ('11', 'Hip / upper leg'),
        ('12', 'Knee / lower leg / foot'),
        ('13', 'Entire body');
    ''')

    # injury_type
    op.execute('''
        INSERT INTO "TAR"."injury_type" (code, description) VALUES
        ('00', 'Unknown'),
        ('01', 'None'),
        ('02', 'Abrasion'),
        ('03', 'Bruises'),
        ('04', 'Lacerations'),
        ('05', 'Bleeding'),
        ('06', 'Fracture'),
        ('07', 'Dislocation'),
        ('08', 'Burns'),
        ('09', 'Amputations'),
        ('10', 'Concussion'),
        ('11', 'Drowning'),
        ('12', 'Whiplash'),
        ('99', 'Other');
    ''')

    # victim_status
    op.execute('''
        INSERT INTO "TAR"."victim_status" (code, description) VALUES
        ('00', 'Unknown'),
        ('01', 'Apparently Normal'),
        ('02', 'Agitated'),
        ('03', 'Incoherent'),
        ('04', 'Semi-Conscious'),
        ('05', 'Unconscious'),
        ('06', 'Apparently Dead'),
        ('07', 'Natural Cause Death'),
        ('08', 'Victim Of Suicide'),
        ('09', 'Victim Of Homicide');
    ''')

    # taken_to
    op.execute('''
        INSERT INTO "TAR"."taken_to" (code, description) VALUES
        ('UNKN', 'Unknown'),
        ('MEDC', 'Medical Clinic / Ambulance Attendant'),
        ('DOCT', 'Family Doctor'),
        ('MORG', 'Morgue'),
        ('HOME', 'Home'),
        ('OTHR', 'Other'),
        ('HOSP', 'Hospital');
    ''')

    # taken_by
    op.execute('''
        INSERT INTO "TAR"."taken_by" (code, description) VALUES
        ('UNKN', 'Unknown'),
        ('AMBU', 'Ambulance / hospital transport'),
        ('EMER', 'Other emergency vehicle (police, fire department)'),
        ('PVEH', 'Personal vehicle'),
        ('TAXI', 'Bus / taxi'),
        ('OTHR', 'Other');
    ''')

    # injury_classification
    op.execute('''
        INSERT INTO "TAR"."injury_classification" (code, description) VALUES
        ('00', 'Unknown'),
        ('01', 'No apparent injuries'),
        ('02', 'Minor – abrasions, bruises and lacerations was immediately released from the hospital'),
        ('03', 'Serious – overnight at hospital'),
        ('98', 'Not applicable');
    ''')

    op.execute('''
        INSERT INTO "TAR"."collision_scenario" (code, description) VALUES
        ('01', 'Collision on Forest Service or Logging Road'),
        ('02', 'Collision on Industrial Road'),
        ('03', 'Collision occurred on Private Driveway/Land'),
        ('04', 'Workplace Accident'),
        ('05', 'Collision off-road involving ATV, snowmobile, farm machinery etc.'),
        ('06', 'Collision not on public road, incl. airport runways, rec. land/campsite. Excl. sidewalks.'),
        ('07', 'Property damage only, estimated value under $10k (excl. vehicle fires)'),
        ('08', 'None of the scenarios apply (reportable fatal, injury, or property damage over $10k)');
    ''')

    op.execute('''
        INSERT INTO "TAR"."police_district" (id, district_name, prefix) values
        (1, 'SOUTHEAST DISTRICT', 'R'),
        (2, 'NORTH DISTRICT', 'R'),
        (3, 'LOWER MAINLAND DISTRICT', 'R'),
        (4, 'ISLAND DISTRICT', 'R'),
        (5, 'INDEPENDENT FORCES', 'N'),
        (6, 'FNAPS FORCES', 'N'),
        (7, 'OTHER FORCES', 'N');
    ''')

    op.execute('''
        INSERT INTO "TAR"."police_agency" (code, district_id, agency_name, vjur_agency) values
        (101, 1, 'Armstrong Prov', NULL),
        (102, 1, 'Enderby Prov', NULL),
        (103, 1, 'Falkland Prov', NULL),
        (104, 1, 'Kelowna Prov', NULL),
        (105, 1, 'Kelowna Mun', NULL),
        (106, 1, 'Keremeos Prov', NULL),
        (107, 1, 'Lumby Prov', NULL),
        (109, 1, 'Oliver Prov', NULL),
        (110, 1, 'Osoyoos Prov', NULL),
        (111, 1, 'Penticton Prov', NULL),
        (112, 1, 'Penticton Mun', NULL),
        (113, 1, 'Princeton Prov', NULL),
        (114, 1, 'Revelstoke Prov', NULL),
        (115, 1, 'Salmon Arm Prov', NULL),
        (116, 1, 'Salmon Arm Mun', NULL),
        (117, 1, 'Sicamous Prov', NULL),
        (118, 1, 'Vernon Prov', NULL),
        (119, 1, 'Vernon Mun', NULL),
        (121, 1, 'Summerland Mun', NULL),
        (124, 1, 'Revelstoke Mun', NULL),
        (125, 1, 'Coldstream Mun', NULL),
        (126, 1, 'Spallumcheen Mun', NULL),
        (127, 1, 'Lake Country Mun', NULL),
        (203, 1, 'Ashcroft Prov', NULL),
        (204, 1, 'Barriere Prov', NULL),
        (206, 1, 'Chase Prov', NULL),
        (207, 1, 'Clearwater Prov', NULL),
        (208, 1, 'Clinton Prov', NULL),
        (209, 1, 'T’Kumlups Prov', NULL),
        (210, 1, 'Kamloops Mun', NULL),
        (211, 1, 'Lillooet Prov', NULL),
        (212, 1, 'Logan Lake Prov', NULL),
        (213, 1, 'Lytton Prov', NULL),
        (214, 1, 'Merritt Prov', NULL),
        (215, 1, 'Merritt Mun', NULL),
        (301, 1, 'Castlegar Prov', NULL),
        (302, 1, 'Cranbrook Prov', NULL),
        (303, 1, 'Cranbrook Mun', NULL),
        (305, 1, 'Creston Prov', NULL),
        (306, 1, 'Fernie Prov', NULL),
        (309, 1, 'Golden/Field Prov', NULL),
        (310, 1, 'Grand Forks Prov', NULL),
        (311, 1, 'Columbia Valley Prov', NULL),
        (312, 1, 'Kaslo Prov', NULL),
        (313, 1, 'Kimberley Prov', NULL),
        (314, 1, 'Kimberley Mun', NULL),
        (315, 1, 'Midway Prov', NULL),
        (316, 1, 'Nakusp Prov', NULL),
        (317, 1, 'Nelson Prov', NULL),
        (318, 1, 'Slocan Lake Prov', NULL),
        (321, 1, 'Salmo Prov', NULL),
        (322, 1, 'Elk Valley Prov (Sparwood)', NULL),
        (323, 1, 'Trail and Greater District Prov', NULL),
        (324, 1, 'Trail Mun', NULL),
        (327, 1, 'Castlegar Mun', NULL),
        (329, 1, 'Elkford Prov', NULL),
        (201, 2, 'Alexis Creek Prov', NULL),
        (202, 2, 'Anahim Lake Prov', NULL),
        (216, 2, 'One Hundred Mile House Prov', NULL),
        (218, 2, 'Valemount Prov', NULL),
        (219, 2, 'Williams Lake Prov', NULL),
        (221, 2, 'Williams Lake Mun', NULL),
        (222, 2, 'Quesnel Prov', NULL),
        (223, 2, 'Quesnel Mun', NULL),
        (224, 2, '100 Mile House Mun', NULL),
        (225, 2, 'Ashcroft Mun', NULL),
        (226, 2, 'Cache Creek Prov', NULL),
        (227, 2, 'Lillooet Mun', NULL),
        (228, 2, 'Logan Lake Mun', NULL),
        (229, 2, 'Barriere Mun', NULL),
        (230, 2, 'Clearwater Mun', NULL),
        (231, 2, 'Chase Mun', NULL),
        (232, 2, 'Clinton Mun', NULL),
        (233, 2, 'T’Kumlups Mun', NULL),
        (234, 2, 'Merritt Mun (City)', NULL),
        (235, 2, 'Spallumcheen Prov', NULL),
        (236, 2, 'Coldstream Prov', NULL),
        (237, 2, 'Lake Country Prov', NULL),
        (501, 2, 'Burns Lake Prov', NULL),
        (502, 2, 'Chetwynd Prov', NULL),
        (503, 2, 'Dawson Creek Prov', NULL),
        (504, 2, 'Dawson Creek Mun', NULL),
        (505, 2, 'Fort Nelson Prov', NULL),
        (506, 2, 'Fort St. James Prov', NULL),
        (507, 2, 'Fort St. John Prov', NULL),
        (508, 2, 'Fort St. John Mun', NULL),
        (509, 2, 'Fraser Lake Prov', NULL),
        (510, 2, 'Hudson’s Hope Prov', NULL),
        (511, 2, 'Mackenzie Prov', NULL),
        (512, 2, 'McBride Prov', NULL),
        (513, 2, 'Prince George Prov', NULL),
        (514, 2, 'Quesnel Prov', NULL),
        (515, 2, 'Quesnel Mun', NULL),
        (517, 2, 'Vanderhoof Prov', NULL),
        (518, 2, 'Wells Prov', NULL),
        (521, 2, 'Prince George Mun', NULL),
        (522, 2, 'Mackenzie Mun', NULL),
        (524, 2, 'Tumbler Ridge Prov', NULL),
        (525, 2, 'Tsay Keh Dene Prov', NULL),
        (526, 2, 'Takla Landing Prov', NULL),
        (601, 2, 'Atlin Prov', NULL),
        (602, 2, 'Bella Coola Prov', NULL),
        (604, 2, 'New Hazelton Prov', NULL),
        (605, 2, 'Houston Prov', NULL),
        (606, 2, 'Kitimat Prov', NULL),
        (607, 2, 'Kitimat Mun', NULL),
        (608, 2, 'Masset Prov', NULL),
        (610, 2, 'Prince Rupert Prov', NULL),
        (611, 2, 'Prince Rupert Mun', NULL),
        (612, 2, 'Queen Charlotte City Prov', NULL),
        (613, 2, 'Smithers Prov', NULL),
        (614, 2, 'Stewart Prov', NULL),
        (615, 2, 'Dease Lake Prov', NULL),
        (616, 2, 'Terrace Prov', NULL),
        (617, 2, 'Terrace Mun', NULL),
        (619, 2, 'Granisle Prov', NULL),
        (620, 2, 'Bella Bella Prov', NULL),
        (621, 2, 'Lisims/Nass Valley Prov', NULL),
        (622, 2, 'Smithers Mun', NULL),
        (703, 3, 'Agassiz Prov', NULL),
        (704, 3, 'Burnaby Mun', NULL),
        (705, 3, 'Boston Bar Prov', NULL),
        (706, 3, 'Chilliwack Prov', NULL),
        (707, 3, 'Chilliwack Mun', NULL),
        (709, 3, 'Coquitlam Prov', NULL),
        (710, 3, 'Coquitlam Mun', NULL),
        (711, 3, 'Port Coquitlam Mun', NULL),
        (712, 3, 'Ridge Meadows Prov', NULL),
        (713, 3, 'Maple Ridge Mun', NULL),
        (714, 3, 'Hope Prov', NULL),
        (715, 3, 'Gibsons Landing Prov', NULL),
        (716, 3, 'Langley City Mun', NULL),
        (717, 3, 'Langley Township Mun', NULL),
        (718, 3, 'Mission Prov', NULL),
        (719, 3, 'Mission Mun', NULL),
        (720, 3, 'North Vancouver City Mun', NULL),
        (721, 3, 'North Vancouver District Mun', NULL),
        (722, 3, 'Richmond Mun', NULL),
        (723, 3, 'Sechelt Prov', NULL),
        (724, 3, 'Squamish Prov', NULL),
        (725, 3, 'Squamish Mun', NULL),
        (726, 3, 'Surrey Mun', NULL),
        (727, 3, 'University Prov', NULL),
        (729, 3, 'White Rock Mun', NULL),
        (737, 3, 'Pemberton Prov', NULL),
        (738, 3, 'Whistler Prov', NULL),
        (739, 3, 'Surrey Prov', NULL),
        (741, 3, 'Pitt Meadows Mun', NULL),
        (742, 3, 'Bowen Island Prov', NULL),
        (743, 3, 'Sechelt Mun', NULL),
        (745, 3, 'Hope Mun', NULL),
        (747, 3, 'Whistler Mun', NULL),
        (748, 3, 'North Vancouver Prov', NULL),
        (802, 4, 'West Shore Prov', NULL),
        (803, 4, 'Duncan Prov', NULL),
        (804, 4, 'North Cowichan Mun', NULL),
        (805, 4, 'Gabriola Island Prov', NULL),
        (806, 4, 'Saltspring Island Prov', NULL),
        (807, 4, 'Ladysmith Prov', NULL),
        (808, 4, 'Lake Cowichan Prov', NULL),
        (809, 4, 'Nanaimo Prov', NULL),
        (810, 4, 'Nanaimo Mun', NULL),
        (811, 4, 'Outer Gulf Islands Prov', NULL),
        (812, 4, 'Shawnigan Lake Prov', NULL),
        (813, 4, 'Sidney Prov', NULL),
        (814, 4, 'Sidney Mun', NULL),
        (815, 4, 'Sooke Prov', NULL),
        (820, 4, 'North Saanich Mun', NULL),
        (821, 4, 'Colwood Mun', NULL),
        (822, 4, 'View Royal Mun', NULL),
        (823, 4, 'Langford Mun', NULL),
        (824, 4, 'Ladysmith Mun', NULL),
        (827, 4, 'Sooke Mun', NULL),
        (901, 4, 'Alert Bay Prov', NULL),
        (902, 4, 'Campbell River Prov', NULL),
        (903, 4, 'Campbell River Mun', NULL),
        (904, 4, 'Comox Mun', NULL),
        (905, 4, 'Comox Valley Prov', NULL),
        (906, 4, 'Courtenay Mun', NULL),
        (907, 4, 'Nootka Sound (Gold River) Prov', NULL),
        (908, 4, 'Oceanside Prov (Parksville)', NULL),
        (909, 4, 'Port Alberni Prov', NULL),
        (910, 4, 'Port Alberni Mun', NULL),
        (911, 4, 'Port Alice Prov', NULL),
        (912, 4, 'Port Hardy Prov', NULL),
        (913, 4, 'Port McNeill Prov', NULL),
        (914, 4, 'Powell River Prov', NULL),
        (915, 4, 'Powell River Mun', NULL),
        (916, 4, 'Quadra Island Prov', NULL),
        (917, 4, 'Sayward Prov', NULL),
        (919, 4, 'Tofino Prov', NULL),
        (920, 4, 'Ucluelet Prov', NULL),
        (922, 4, 'Parksville Mun', NULL),
        (924, 4, 'Texada Island Prov', NULL),
        (925, 4, 'Qualicum Beach Mun', NULL),
        (401, 5, 'Vancouver Mun', NULL),
        (402, 5, 'Victoria and Esquimalt Mun', NULL),
        (403, 5, 'Saanich Mun', NULL),
        (404, 5, 'Central Saanich Mun', NULL),
        (406, 5, 'Oak Bay Mun', NULL),
        (407, 5, 'Delta Mun', NULL),
        (408, 5, 'Abbotsford Mun', NULL),
        (409, 5, 'New Westminster Mun', NULL),
        (410, 5, 'West Vancouver Mun', NULL),
        (411, 5, 'Nelson Mun', NULL),
        (412, 5, 'Port Moody Mun', NULL),
        (1101, 6, 'Stl’atl’imx Tribal Police', NULL),
        (1103, 6, 'Kitasoo/Xaixais Public Safety Department', NULL),
        (1003, 7, 'CN Police (eff. 1994)', NULL),
        (1004, 7, 'CP Police (eff. 1994)', NULL);
    ''')


def downgrade():
    # Truncate all code tables in TAR schema (in reverse dependency order if needed)
    op.execute('TRUNCATE TABLE "TAR"."injury_classification" RESTART IDENTITY CASCADE;')
    op.execute('TRUNCATE TABLE "TAR"."taken_by" RESTART IDENTITY CASCADE;')
    op.execute('TRUNCATE TABLE "TAR"."taken_to" RESTART IDENTITY CASCADE;')
    op.execute('TRUNCATE TABLE "TAR"."victim_status" RESTART IDENTITY CASCADE;')
    op.execute('TRUNCATE TABLE "TAR"."injury_type" RESTART IDENTITY CASCADE;')
    op.execute('TRUNCATE TABLE "TAR"."injury_location" RESTART IDENTITY CASCADE;')
    op.execute('TRUNCATE TABLE "TAR"."ejection" RESTART IDENTITY CASCADE;')
    op.execute('TRUNCATE TABLE "TAR"."safety_equipment" RESTART IDENTITY CASCADE;')
    op.execute('TRUNCATE TABLE "TAR"."position" RESTART IDENTITY CASCADE;')
    op.execute('TRUNCATE TABLE "TAR"."vehicle_use" RESTART IDENTITY CASCADE;')
    op.execute('TRUNCATE TABLE "TAR"."vehicle_type" RESTART IDENTITY CASCADE;')
    op.execute('TRUNCATE TABLE "TAR"."pre_collision_action" RESTART IDENTITY CASCADE;')
    op.execute('TRUNCATE TABLE "TAR"."damage_severity" RESTART IDENTITY CASCADE;')
    op.execute('TRUNCATE TABLE "TAR"."damage_location" RESTART IDENTITY CASCADE;')
    op.execute('TRUNCATE TABLE "TAR"."contributing_factors" RESTART IDENTITY CASCADE;')
    op.execute('TRUNCATE TABLE "TAR"."entity_type" RESTART IDENTITY CASCADE;')
    op.execute('TRUNCATE TABLE "TAR"."pedestrian_action" RESTART IDENTITY CASCADE;')
    op.execute('TRUNCATE TABLE "TAR"."pedestrian_location" RESTART IDENTITY CASCADE;')
    op.execute('TRUNCATE TABLE "TAR"."primary_collision_occurrence" RESTART IDENTITY CASCADE;')
    op.execute('TRUNCATE TABLE "TAR"."location_of_first_contact" RESTART IDENTITY CASCADE;')
    op.execute('TRUNCATE TABLE "TAR"."type_of_collision" RESTART IDENTITY CASCADE;')
    op.execute('TRUNCATE TABLE "TAR"."lighting_condition" RESTART IDENTITY CASCADE;')
    op.execute('TRUNCATE TABLE "TAR"."weather_condition" RESTART IDENTITY CASCADE;')
    op.execute('TRUNCATE TABLE "TAR"."roadway_condition" RESTART IDENTITY CASCADE;')
    op.execute('TRUNCATE TABLE "TAR"."roadway_character" RESTART IDENTITY CASCADE;')
    op.execute('TRUNCATE TABLE "TAR"."traffic_control" RESTART IDENTITY CASCADE;')
    op.execute('TRUNCATE TABLE "TAR"."road_type" RESTART IDENTITY CASCADE;')
    op.execute('TRUNCATE TABLE "TAR"."land_usage" RESTART IDENTITY CASCADE;')
    op.execute('TRUNCATE TABLE "TAR"."speed_zone" RESTART IDENTITY CASCADE;')
    op.execute('TRUNCATE TABLE "TAR"."collision_location" RESTART IDENTITY CASCADE;')
    op.execute('TRUNCATE TABLE "TAR"."traffic_flow" RESTART IDENTITY CASCADE;')
    op.execute('TRUNCATE TABLE "TAR"."road_class" RESTART IDENTITY CASCADE;')
    op.execute('TRUNCATE TABLE "TAR"."police_agency" RESTART IDENTITY CASCADE;')
    op.execute('TRUNCATE TABLE "TAR"."police_district" RESTART IDENTITY CASCADE;')
