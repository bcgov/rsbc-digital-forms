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
