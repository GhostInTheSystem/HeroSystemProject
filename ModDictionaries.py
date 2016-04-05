absorptionMods = {'Increased Maximum': 'adv.25', "Varying Effect": 'adv.75', 'Limited Phenomenon (Rare)': 'lim1', 'Limited Phenomenon (Uncommon)': 'lim.75', 'Limited Phenomenon (Common)': 'lim.5',
                  'Limited Phenomenon (Very Common)': 'lim.25'}
aidMods = {'Only Others': 'lim.5', 'Only Self': 'lim1'}
barrierMods = {'Non=Anchored': 'num10', 'Opaque to One Sense': 'num5', 'Opaque to One Sense Group': 'num10', 'Allocatable': 'adv.25', 'Backlash': 'adv.5', 'Cannot Be Escaped With Teleportation': 'adv.25',
               'Configurable': 'adv.25', 'Counteracts Indirect': 'adv.25', 'Mobile': 'adv.25', 'One-Way Transparent (One Attack)': 'adv.25', 'One-Way Transparent (All Attacks)': 'adv.25', 'Cannot Englobe': 'lim.25',
               'Feedback': 'lim1', 'Nonresistant Defense': 'lim.25', 'Restricted Shape': 'lim.25'}
#5 base pools
blastMods = {'STUN Only': 'lim0'}
changeEnvironmentMods={'Long-lasting': 'num1', 'Varying Combat Effects': 'num10', 'Varying Effect (Very Limited)': 'adv.25', 'Varying Effect (Limited)': 'adv.5', 'Varying Effect (Broad)': 'adv1', 'No Range': 'lim.5'}
clairsentienceMods={'Extra Sense Group': 'num10', 'Extra Sense': 'num5', 'Precognition': 'num20', 'Retrocognition': 'num20', 'Mobile': 'num5', 'Multiple Perception Points': 'num5', 'Double Range': 'num5',
                    'Attack Roll Required': 'lim.25', 'Blackout': 'lim.5', 'Fixed Perception Point': 'lim1', 'Only Through The Sense of Others': 'lim.5', 'One Sense Only': 'lim.25',
                    'Precognition/Retrocognition Only': 'lim1', 'Only Through Dreams': 'lim1', 'Time Modifiers': 'lim.25', 'Vague And Unclear': 'lim.25'}
#add sense modifiers
clingingMods={'Cannot Resist Knockback': 'lim.25'}
damageNegationMods={'Nonresistant': 'lim.25', 'STUN/BODY Only': 'lim.5'}
damageReduction={'25% Nonresistant': 'num10', '25% Resistant': 'num15', '50% Nonresistant': 'num20', '50% Resistant': 'num30', '75% Nonresistant': 'num40', '75% Resistant': 'num60', 'STUN/BODY Only': 'lim.25',
                 'Set Effect (1/4)': 'lim.25', 'Set Effect (1/2)': 'lim.5', 'Set Effect (3/4)': 'lim.75', 'Set Effect (1)': 'lim.25'}
darknessMods={'Targeting Sense Group': 'num10', 'Single Targeting Sense': 'num5', 'Nontargeting Sense Group': 'num5', 'Single Nontargeting Sense': 'num3'}
densityIncreaseMods={'No Defense Increase': 'lim.25', 'No STR Increase': 'lim1'}
desolidificationMods={'Affects Physical World': 'adv1', 'Cannot Pass Through Solid Objects': 'lim.5', 'Doesn\'yt Protect Against Damage': 'lim1', 'Only to Protect Against [Limited Type of Attack]': 'lim1'}
drainMods={'Suppress': 'lim.5'}
duplicationMods={'Double Number of Duplicates': 'num5', "Easy Recombination (Half Phase)": 'num5', 'Easy Recombination (Zero Phase)': 'num10', 'Altered Duplicate (1-25%)': 'adv.25', 'Altered Duplicate (26-50%)': 'adv.5',
                 'Altered Duplicate (50-100%)': 'adv1', 'Ranged Recombination': 'adv.25', 'Rapid Duplication': 'adv.25', 'Cannot Recombine': 'lim0', 'Feedback (All Damage, All Duplicates)': 'lim1',
                 'Feedback  (STUN Only, All Duplicates)': 'lim.5', 'Feedback (Only One Duplicate)': 'lim.25', 'No Averaging': 'lim0'}
enduranceReserve={'Limited Recovery': 'lim2', 'Restricted Use': 'lim.25', 'Slow Recovery': 'lim1'}
#2 base pools
detectMods={'Single Thing': 'num3', 'Class of Things': 'num5', 'Large Class of Things': 'num10', 'Each Extra Thing/Class of Things': 'num5'}
sensesMods={'Active Sonar': 'num15', 'High Range Radio Perception': 'num12', 'Infrared Perception': 'num5', 'Mental Awareness': 'num5', 'Nightvision': 'num5', 'Radar': 'num15', 'Radio Perception': 'num8',
            'Radio Perception/Transmission': 'num10', 'Spatial Awareness': 'num32', 'Ultrasonic Perception': 'num3', 'Ultraviolet Perception': 'num5', 'Adjacent (Fixed, Single)', 'num2', 'Adjacent (Fixed, Group)': 'num3',
            'Adjacent (Variable, Single)': 'num3', 'Adjacent (Variable, Group)': 'num5', 'Concealed (1 Level)': 'num1', 'Discriminatory (Single Sense)': 'num5', 'Discriminatory (Sense Group)': 'num10',
            'Analyze (Single Sense)': 'num5', 'Analyze (Sense Group)': 'num10', 'Dimensional (Single Dimension, Single Sense)': 'num5', 'Dimensional (Single Dimension, Sense Group)': 'num10',
            'Dimensional (Group of Dimensions, Single Sense)': 'num10', 'Dimensional (Group of Dimensiosn, Sense Group)': 'num20', 'Dimensional (Any Dimension, Single Sense)': 'num15',
            'Dimensional (Any Dimension, Sense Group)': 'num25', '240-Perception (Single Sense)': 'num2', '240-Perception (Sense Group)': 'num5', '240-Perception (Any Sense)': 'num10',
            '360-Perception (Single Sense)': 'num5', '360-Perception (Sense Group)': 'num10', '360-Perception (Any Sense)': 'num25', 'Magnification (Single Sense)': 'num3', 'Magnification (Sense Group)': 'num5',
            'Penetrative (Partial, Single)': 'num5', 'Penetrative (Partial, Group)': 'num10', 'Penetrative (Full, Single)': 'num10', 'Penetrative (Full, Group)': 'num15', 'Range (Single)': 'num5',
            'Ranged (Group)':'num10',  'Rapid (Single)': 'num3', 'Rapid (Group)': 'num5', 'Telescopic (Single)': 'num1', 'Telescopic (Group)': 'num3', 'Tracking (Single)': 'num5', 'Tracking (Group)': 'num10',
            'Transmit (Single)': 'num2', 'Transmit (Group)': 'num5', 'No Direction': 'adv.5'}
#redo
entangleMods={'Additional BODY': 'num5', 'Additional Defense': 'num5', 'Stops a Sense (Single)', 'num5', 'Stop a Sense (Group)': 'num10', 'Backlash': 'adv.5', 'Cannot Be Escaped With Teleportation': 'adv.25',
              'Entangle and Character Both Take Damage': 'adv.25', 'Takes No Damage From Attacks (Group)': 'adv.25', 'Takes No Damage From Attacks (Any)': 'adv.5',
              'Takes No Damage From Attacks (No Effects from Outside)': 'adv1', 'Doesn\'t Prevent The Use of Accessible Foci': 'lim1', 'Has 1 BODY': 'lim.5', 'No Defense': 'lim1.5', 'Nonresistant Defense': 'lim.25',
              'Set Effect (Hands/Feet Only)': 'lim1', 'Susceptible (Uncommon/Very Difficult to Determine)': 'lim.25', 'Susceptible (Common/Difficult to Determine)': 'lim.5',
              'Susceptible (Very Common/Easy to Determine)': 'lim1', 'Vulnerable (Uncommon/Very Difficult to Determine)': 'lim.25', 'Vulnerable (Common/Difficult to Determine)': 'lim.5',
              'Vulnerable (Very Common/Easy to Determine)': 'lim1'}
extraDimensionalMovementMods={'Related Group of Dimensions': 'num5', 'Any Dimension': 'num10', 'Any Location within the Dimension': 'num5', 'Only Corresponding Location': 'num-3',
                              'Travel to Single Moment in Time': 'num20', 'Travel to Related Moments in Time': 'num5', 'Travel Back or Forward 1 Turn': 'num1', '+1 Time Chart Increment': 'num1',
                              'Time Travel to Single Location': 'num2', 'Time Travel to Group of Locations': 'num5', 'Time Travel to any Location': 'num10', 'Increased Mass': 'num5', 'Safe Blind Travel': 'adv.25'}
extraLimbsMods={'Limited Manipulation': 'lim.25'}
ftlTravelMods={'x2 Velocity': 'num2', 'Instant Lightspeed': 'num10'}
flashMods={'Additional Targeting Sense': 'num5', 'Additional Targeting Sense Group': 'num10', 'Additional Nontargeting Sense Group': 'num5', 'Additional Nontargeting Sense': 'num3',
           'Doesn\'t Work Against Desolidified Characters': 'lim.25'}
flashDefenseMods={'Resistant': 'adv.5'}
flightMods={'Usable [As Second Mode of Movement': 'adv.25', 'Cannot Hover (2m)': 'lim.25', 'Cannot Hover (Half Move)': 'lim.5', 'Gliding only': 'lim1', 'Only in Contact With a Surface': 'lim.25'}
growthMods={'Enormous': 'num25', 'Huge': 'num65', 'Gigantic': 'num95', 'Gargantuan': 'num125', 'Colossal': 'num190'}
healingMods={'Can Heal Limbs': 'num5', 'Resurrection': 'num20', 'Decreased Re-use Duration': 'adv.25', 'Doesn\'t Work on (Rare)': 'lim.25', 'Doesn\'t Work on (Uncommon)': 'lim.5', 'Doesn\'t Work on (Common)': 'lim.75',
             'Doesn\'t Work on (Very Common)': 'lim1', 'Resurrection Only': 'lim.5'}
imageMods={'Targeting Sense Group': 'num10', 'Targeting Sense': 'num5', 'Nontargeting Sense Group': 'num5', 'Nontargeting Sense': 'num3', 'Difficult to Alter (Half Phase)': 'lim.25',
           'Difficult to Alter (Full Phase)': 'lim.5', 'Only to Create Light': 'lim1', 'Set Effect': 'lim1'} 
invisibilityMods={'Extra Targeting Sense Group': 'num10', 'Extra Targeting Sense': 'num5', 'Extra Nontargeting Sense Group': 'num5', 'Extra Nontargeting Sense': 'num3', 'No Fringe': 'num10', 'Bright Fringe': 'lim.25',
                  'Chameleon': 'lim.5', 'Only When Not Attacking': 'lim.5'} 
killingAttackMods={'Increased STUN Multiplier': 'adv.25', 'Decreased STUN Multiplier': 'lim.25', 'No STR Bonus': 'lim.5'}
leapingMods={'Accurate Leap': 'num5', 'Forward Movement Only': 'lim1'}
lifeSupport={'1 Level Extended Breathing': 'num1', 'Expanded Breathing': 'num5', 'Self-Contained Breathing': 'num10', '1 Level Diminished Eating': 'num1', '1 Level Diminished Sleep': 'num1',
             'Safe Environment (Low Pressure)': 'num2', 'Safe Environment (High Pressure)': 'num1', 'Safe Environment (High Radiation)': 'num1', 'Safe Environment (Intense Cold)': 'num1',
             'Safe Environment (Intense Heat)': 'num1', '1 Level Longevity': 'num1', '1 Level Immunity': 'num1', 'Immunity to all Terrestrial Diseases or Poisons': 'num5'}
mentalIllusionMods={'Cannot Cause Harm': 'lim.25', 'Depends on Character\'s Knowledge': 'lim.5', 'Limited By Senses (Nontargetting)': 'lim.25', 'Limited By Senses (Targetting)': 'lim.5', 'No Concious Control': 'lim1',
                    'Self Only': 'lim1'}
mindControlMods={'Telepathic': 'adv.25', 'Literal Interpretation': 'lim.25', 'Set Effect': 'lim.5'}
mindLinkMods={'Single Mind as Target': 'num5': 'Group of Minds (Target)': 'num10', 'Any Mind (Target)': 'num15', 'x2 Minds at Once': 'num5', 'Unlimited Range in Dimension': 'num5',
              'Unlimited Range in Any Dimension': 'num10', 'No LOS Needed': 'num10', 'Psychic Bond': 'num5', 'Floating Psychic Bond': 'num10', 'Feedback (STUN Only)': 'lim1', 'Feedback (STUN and BODY)': 'lim2',
              'Only With Others Who Have Mind Link': 'lim1'}
mindScanMods={'+1 OMCV': 'num2', 'One-Way Link': 'adv1', 'Partial Lock-On': 'adv.5', 'Cannot Attack Through Link (Neither, Attack)': 'lim.5', 'Cannot Attack Through Link (Neither, Attack/Communicate)': 'lim1',
              'Cannot Attack Through Link (Only Self, Attack/Communicate)': 'lim1.5', 'Partial Effect': 'lim.5'}
muliformMods={'x2 Forms': 'num5', 'Instant Change': 'num5', 'Costs Endurance to Change': 'lim.5', 'Costs Endurance to Maintain': 'lim1', 'Personality Loss (1 Level up the Time Chart from 1 Month)': 'lim.25',
              'Reversion (True More Powerful)': 'adv.5', 'Reversion (True Less Powerful)': 'lim.5', 'Reversion (Equal)': 'lim0'}
powerDefenseMods={'Resistant': 'adv.5'}
reflectionMods={'Any Target': 'adv.5', 'Feedback': 'lim1'}
regenerationMods={'Up In Frequency (Time Chart)': 'num2', 'Can Heal Limbs': 'num5', 'Resurrection': 'num20', 'Doesn\'t Work on (Rare)': 'lim.25', 'Doesn\'t Work on (Uncommon)': 'lim.5',
                  'Doesn\'t Work on (Common)': 'lim.75', 'Doesn\'t Work on (Very Common)': 'lim1', 'Resurrection': 'lim2'}
resistantProtection={'Impermeable': 'lim0', 'Protects Carried Items': 'num10', 'Allocatable': 'adv.25'}
runningMods={'Only on Appropriate Terrain': 'lim.5'}
shapeshiftMods={'Sight': 'num8', 'Hearing or Touch': 'num5', 'Mental, Radio, or Smell/Taste': 'num2', 'Any Single Unusual Sense': 'num3', 'Up to 4 Shapes': 'num3', 'Limited Group of Shapes': 'num5', 'Any Shape': 'num10', 
                'Cellular (External Only)': 'num5', 'Cellular (Full)': 'num10', 'Imitation': 'num10', 'Instant Change': 'num5', 'Makeover': 'num5', 'Affects Body Only': 'lim.5', 'Limited Effect': 'lim.25'}
shrinkingMods={'Normal Mass (No Choice)': 'adv.5', 'Normal Mass (Choice)': 'adv1', 'Easily Perceived': 'lim.25'}
stretchingMods={'One Degree of Stretching Dimensions': 'num5', 'Does Not Cross Intervening Space': 'adv.25', 'Always Direct': 'lim.25', 'Cannot Do Damage': 'lim.5', 'Limited Body Parts': 'lim.25',
                'No Noncombat Stretching': 'lim.25', 'Only To Cause Damage': 'lim.5', 'Range Modifier Applies': 'lim.25'}
summonMods={'2x Summoned Servants': 'num1', 'Amicable (Friendly)': 'adv.25', 'Amicable (Loyal)': 'adv.5', 'Amicable (Devoted)': 'adv.75', 'Amicable (Slavish)': 'adv1', 'x2 Tasks': 'adv.25',
            'Expanded Class (Very Limited)': 'adv.25', 'Expanded Class (limited)': 'adv.5', 'Expanded Class (Any)': 'adv1', 'Specific Being': 'adv1', 'Weak-Willed (-2)': 'adv.25', 'Weak-Willed (-4)': 'adv.5',
            'Antagonistic (Annoyed)': 'lim.25', 'Antagonistic (Hostile)': 'lim.5', 'Antagonistic (Violent)': 'lim.75', 'Arrived Under Own Power': 'lim.5', 'Fewer Tasks': 'lim.25', 'Strong-Willed (+2)': 'lim.25',
            'Strong-Willed (+4)': 'lim.5', 'Summoned Being Must Inhabit Locale': 'lim.5'}
swimmingMods={'Surface Only': 'lim1'}
telekinesisMods={'Fine Manipulation': 'num10', 'Affects Whole Object': 'lim.25', 'Only Works on (Limited)': 'lim.5', 'Only Works on (Very Limited)': 'lim1'}
telepathyMods={'Broadcast/Recieve Only': 'lim.5', 'Communication Only': 'lim.25', 'Empathy (All Emotions)': 'lim.5', 'Empathy (Single Emotion)': 'lim1', 'Feedback (STUN Only)': 'lim1',
               'Feedback (STUN and BODY)': 'lim2', 'Language Barrier': 'lim.5', 'Surface Thoughts Only': 'lim.25'}
teleportationMods={'2x mass': 'num5', '+1 Fixed Location': 'num1', '+1 Floating Fixed Point': 'num5', 'Gate': 'lim.5', 'No Relative Velocity': 'num10', 'Position Shift': 'num5', 'Safe Aquatic Teleport': 'num5',
                   'Safe Blind Teleport': 'adv.25', 'Can Only Teleport to Fixed Locations (Has no Floating Fixed)': 'lim1', 'Can Only Teleport to Fixed Locations (Has Floating Fixed Locations)': 'lim.5',
                   'Must Pass Through Intervening Space': 'lim.25'}
transformMods={'Improved Results Group (Limited)': 'adv.25', 'Improved Results Group (All)': 'adv1', 'Partial Transform': 'adv.5', 'Variable Healing Method': 'adv.25', 'All Or Nothing': 'lim.5',
               'Slighty Limited Target': 'lim.25', 'Limited Target': 'lim.5', 'Very Limited Target': 'lim1', 'Rapid Healing': 'lim.25'}
tunnelingMods={'Fill In': 'num10', 'Limited Medium': 'lim.5', 'Very Limited Medium': 'lim1'}
#3 base pools
affectsDesolidifiedMods={'Affects Desolidified (All Forms)': 'adv.5', 'Affects Desolidified (Specififc Form)': 'adv.5'}
alternateCombatValueMods={'Mental Power Uses OCV': 'adv.25', 'Mental Power Attacks DCV': 'lim.25', 'Non-Mental Power uses OMCV': 'adv0', 'Non-Mental Power Attacks DMCV': 'adv.25'}
areaOfEffectMods={'Area of Effect: 4m Radius/8m Cone/16m Line/2m Surface/2x2m Any Area': 'adv.25', 'Area of Effect: Explosion': 'adv-.5', 'Area of Effect: Nonselective': 'adv-.25',
                  'Area of Effect: Selective': 'adv.25', 'Area of Effect: Mobile': 'adv.5', 'Area of Effect: Accurate': 'adv.25', 'Area of Effect: Thin Cone': 'adv-.25', 'Area of Effect: Fixed Shape': 'adv-.25'}
attackVersusAlternateDefenseMods={'One Step Up the AVAD table': 'lim.5', 'One Step Down the AVAD table': 'adv.5'}
autofireMods={'Autofire: 2-3 Shots': 'adv.25', 'Autofire: Up to 5 Shots': 'adv.5', 'Autofire: Double Maximum Shots': 'adv.5', 'Autofire Against Non-Normal Defenses/Does Not Require a Normal Attack Roll': 'adv1'}
cumulativeMods={'Cumulative': 'adv.5', 'Cumulative: Double Max Points': 'adv.25'}
damageOverTimeMods={'Damage Over Time': 'adv1': 'Damage Over Time: Down One on the Damage Increments Chart': 'adv.25', 'Damage Over Time: Damage Every Segment': 'adv2',
                'Damage Over Time: Damage Every Other Segment': 'adv1.5', 'Damage over Time: Damage Every Three Segments': 'adv1', 'Damage Over Time: Damage Every Four Segments': 'adv.5':
                'Damage Over Time: Damage Every Six Segments': 'adv.5', 'Damage Over Time: Damage Every 30 Segments': 'adv-.25', 'Damage Over Time: Damage Every Minute': 'adv-.5',
                'One Step Down the Time Between Damage Increments Chart Beyond 1 Minute': 'adv-.5'}
delayedEffectMods={'Delayed Effect': 'adv.25', 'Delayed Effect: Double Number of Activated Powers': 'adv.25'}
durationAdvantagesMods={'Constant': 'adv.5', 'Persistent': 'adv.25', 'Inherent': 'adv.25'}
holeInTheMiddleMods={'Hole in the Middle: Fixed Size': 'adv.25', 'Hole in the Middle: Variable Size': 'adv.5'}
indirectMods={'Indirect: Fixed Source Point': 'adv.25', 'Indirect: Variable Source Points': 'adv.5', 'Indirect: Fixed Indirect Path of Power': 'adv.25', 'Indirect: Variable Indirect Path of Power': 'adv.5'}
invisiblePowerEffectsMods={'Obvious to Inobvious (One Sense Group)': 'adv.25', 'Obvious to Invisible (One Sense Group)': 'adv.5', 'Inobvious to Invisible (One Sense Group)': 'adv.25',
                           'Effect of Power Inobvious to Target': 'adv.25', 'Effect of Power Inobvious to Others': 'adv.25', 'Effect of Power Invisible to Target': 'adv.5', 'Effect of Power Invisible to Others': 'adv.5'}
megascaleMods={'Megascale': 'adv1', 'Megascale: Additional Level': 'adv.25', 'Megascale: Unalterable Scale': 'adv-.25'}
rangeAdvantagesMods={'Double Maximum Range': 'adv.25', 'LOS Range': 'adv.5', 'Half Range Modifier': 'adv.25', 'No Range Modifier': 'adv.5'}
rangedMods={'Ranged': 'adv.5', 'Ranged: Limited Range': 'adv.25', 'Ranged: Range Based on Strength': 'adv.25'}
reducedEnduranceMods={'Half Endurance Cost': 'adv.25', 'No Endurance Cost': 'adv.5', 'Costs Endurance Only to Activate': 'adv.25'}
stickyMods={'Sticky': 'adv.5', 'Sticky (Freeing one Victim Frees All)': 'adv.25'}
timeLimitMods={'Time Limit Up One Level (Instant/Constant Power)': 'adv.25', 'Time Limit Down One (Persistent)': 'lim.25'}
transdimensionalMods={'Transdimensional: Single Dimension': 'adv.5', 'Transdimensional: Group of Dimensions': 'adv.75', 'Transdimensional: Any Dimension': 'adv1'}
triggerMods={'Trigger: Fixed': 'adv.25', 'Trigger: Variable': 'adv.5', 'Trigger: Zero-Time Action': 'adv.25', 'Trigget: Character Does not Control Activation': 'adv-.25', 'Trigger: 2 Simultaneous Triggers': 'adv.25',
             'Trigger: Three or More Simultaneous Triggers': 'adv.5', 'Trigger: Turn to Reset': 'adv-.5', 'Trigger: Full Phase to Reset': 'adv-.25', 'Trigger: Zero Phase to Reset': 'adv-.5',
             'Trigger: Auto-Reset': 'adv-.5', 'Trigger: Has Time Limit': 'adv-.25', 'Trigger: Can Misfire': 'adv-.25'}
usableOnOthersMods={'Usable On Others: One Target': 'adv.25', 'Usable on Others: Double Recipients': 'adv.25', 'Usable On Others: One at a Time for Multiple Recepients': 'adv-.25',
                    'Usable On Others: Unwilling Target': 'adv1', 'Usable On Others: Can Take Power Back': 'adv.25', 'Usable On Others: Grantor has Total Control': 'adv.5',
                    'Usable On Others: Grantor Pays Full END Cost': 'adv-.25', 'Usable On Others: Only to Others': 'adv-.5', 'Usable On Others: Limited Range': 'adv.25', 'Usable On Others: Standard Range': 'adv.5',
                    'Usable On Others: Must Maintain LOS': 'adv-.25', 'Usable On Others': 'adv-.5'}
variableSpecialEffectsMods={'Variable Special Effects (Limited Group)': 'adv.25', 'Variable Special Effects (Any)': 'adv.5'}
chargesMods={'1 Charge': 'lim2', '2 Charges': 'lim1.5', 'Each Level of Charges Beyond 2 Before 16': 'lim-.25', 'Each Level of Charges Beyond 13-16': 'adv.25', 'Boostable Charges (2 through 9-12)': 'lim-.25',
             'Boostable Charges (Beyond 9-12)': 'adv.25', 'Recoverable Charges (1)': 'lim-.75', 'Recoverable Charges (2 through 7-8)': 'lim-.5', 'Recoverable Charges 9-12': 'adv.25',
             'Recoverable Charges Beyond 9-12': 'adv.5', 'Charges: Increased Reloading Time': 'lim.25'}
concentrationMods={'Concentration: Half DCV': 'lim.25', 'Concentration: 0 DCV': 'lim.5', 'Concentration: Total Unawareness': 'lim.25', 'Concentration: Half DCV (Constant)': 'lim.5',
                   'Concentration: 0 DCV (Constant)': 'lim1'}
durationLimitationsMods={'Instant': 'lim.5', 'Nonpersistent': 'lim.25'}
enduranceLimitationsMods={'Costs END to Activate': 'lim.25', 'Costs END every Phase to maintain': 'lim.5'}
extraTimeMods={'Delayed Phase': 'lim.25', 'Extra Segment': 'lim.5', 'Full Phase': 'lim.5', 'Extra Phase': 'lim.75', 'One Level of Extra Time (Beyond Extra Phase)': 'lim.5',
               'Can\'t Activate Other Powers while Activating Extra Time Power': 'lim.25'}
focusMods={'IIF': 'lim.25', 'IAF': 'lim.5', 'OIF': 'lim.5', 'OAF': 'lim1', 'Focus: Arrangement': 'lim.25', 'Focus: Bulky': 'lim.5', 'Focus: Immobile': 'lim1', 'Focus: Fragile': 'lim.25',
           'Difficult to obtain new Focus': 'lim.25', 'Very Difficult to obtain New Focus': 'lim.5', 'Extremely Difficult to obtain new Focus': 'lim1'}
gesturesMods={'Gestures: Single Hand': 'lim.25', 'Gestures: Both 



generalMods={'Doesn\'t Work While Duplicate Exists': 'lim.25', 'Power Can Draw END From Character Or Endurance Reserve': 'adv.25', 'Can Only Be Used Through Mind Link': 'lim0', 'Reduced By Shrinking': 'lim.25',
             'Armor Piercing': 'adv.25', '1 Level Difficult to Dispel': 'adv.25', 'Does Body': 'adv1', 'Does Knockback': 'adv.25', 'Double Knockback': 'adv.5', 'Penetrating': 'adv.5', 'Personal Immunity': 'adv.25',
             'Uncontrolled': 'adv.5', 'Always On': 'lim.5'}
