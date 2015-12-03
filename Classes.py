#this class represents the character being created. Most of the variables are just fluff, but the maxima are important for the characteristics
class Character:
	def __init__(self, name):
		self.name = name
		sex = None
		height = None
		mass = None
		skin = None
		hair = None
		eyes = None
		age = None
		species = None
		notes = None
		pointTotal = None
		activePointLimit = None
		complicationPoints = None
		maxima = False
		strMaxima = 20
		dexMaxima = 20
		conMaxima = 20
		intMaxima = 20
		egoMaxima = 20
		preMaxima = 20
		ocvMaxima = 8
		dcvMaxima = 8
		omcvMaxima = 8
		dmcvMaxima = 8
		spdMaxima = 4
		pdMaxima = 8
		edMaxima = 8
		recMaxima = 10
		endMaxima = 50
		bodyMaxima = 20
		stunMaxima = 50
		runMaxima = 20
		swimMaxima = 10
		leapMaxima = 10
		skillMaxima = 13
		numOfPowers = 0
		powers = []
		skills = []
		talents = []
		perks = []
		complications = []
	#methods for easy adding traits to the character class
	def addPower(self, Power):
		self.powers.append(Power)
	def removePower(self, powerName):
		count = 0
		for power in powers:
			if(power.name == powerName):
				powers.pop(count)
			count += 1
	def addSkill(self, Skill):
		self.skills.append(Skill)
	def removeSkill(self, skillName):
		count = 0
		for skill in skill:
			if(skill.name == skillName):
					skills.pop(count)
			count += 1
	def addTalent(self, Talent):
		self.talents.append(Talent)
	def removeTalent(self, talentName):
		count = 0
		for talent in talents:
			if(talent.name == talentName):
				talents.pop(count)
			count += 1
	def addPerk(self, Perk):
		self.perks.append(Perk)
	def removePerk(self, perkName):
		count = 0
		for perk in perks:
			if(perk.name == perkName):
				perks.pop(count)
			count += 1
	def addComplication(self, Complication):
		self.complications.append(Complication)
	def removeComplication(self, complicationName):
		count = 0
		for complication in complications:
			if(complication.name == complicationName):
				complications.pop(count)
			count += 1
#superclass for basically all the cool stuff about character; their characteristics, powers, skills, talents, perks and complications
class Trait:
	def __init__(self, type, name, *poolNames):
		self.type = type
		self.name = name
		self.modifiers = []
		self.basePointPoolNames = []
		self.basePointPoolValues = []
		count = 0
		for poolName in poolNames:
			self.basePointPoolNames.append(poolName)
			self.basePointPoolValues.append(0)
			count += 1
		self.modFlatPoints = 0
		self.advTotal = 0
		self.limTotal = 0
		self.activePoints = (sum(self.basePointPoolValues)+self.modFlatPoints)*(1+self.advTotal)
		self.totalPoints = self.activePoints/(1+self.limTotal)
	#methods for easy adding modifiers to the trait class
	def addMod(self, Modifier):
		self.modifiers.append(Modifier)
	def removeMod(self, modName):
		count = 0
		for mod in modifiers:
			if(mod.name == modName):
				modifiers.pop(count)
			count += 1
#traits in hero system have ultimate customization, so this class will be aggregated by the trait class
class Modifier:
	def __init__(self, id, type, value):
		self.name = name
		self.type = type
		self.value = value
#trait subclass for characteristics
class Characteristic(Trait):
	def __init__(self, name, rollChar, *poolNames):
		Trait.__init__(self, "Characteristic", name, *poolNames)
		self.rollChar = rollChar
		roll = 9
#trait subclass for skills
class Skill(Trait):
	def __init__(self, name, char, rollSkill, *poolNames):
		Trait.__init__(self, "Skill", name, *poolNames)
		self.char = char
		self.rollSkill = rollSkill
		roll = 8
		basePoints = 1
#skill subclass for Knowledge, Professional and Science skills
class KPSSkill(Skill):
	def __init__(self, name, char, kps, field, *poolNames):
		Skill.__init__(self, name, char, True, *poolNames)
		self.kps = kps
		self.field = field
		self.elevenRoll = False
#trait subclass for powers
class Power(Trait):
	def __init__(self, type, name, d6Power, costPerD6, *poolNames):
		Trait.__init__(self, type, name, *poolNames)
		self.d6Power = d6Power
		self.costPerD6 = costPerD6
#power subclass for powers that are part of multipowers
class MPPower(Power):
	def __init__(self, name, d6Power, costPerD6, fixed, *poolNames):
		Power.__init__(self, "MPPower", name, d6Power, costPerD6, *poolNames)
		self.fixed = fixed
#trait subclass for multipowers
class Multipower(Trait):
	def __init__(self, name, *poolNames):
		Trait.__init__(self, "Multipower", name, *poolNames)
		powers = []
		totalPowersCost = 0
	#methods for easy adding powers to the multipower class
	def addPower(self, MPPower):
		self.powers.append(MPPower)
	def removePower(self, powerName):
		count = 0
		for power in powers:
			if(power.name == powerName):
				powers.pop(count)
			count += 1
#trait subclass for variable power point pools
class VPP(Trait):
	def __init__(self, name, pool, control, *poolNames):
		Trait.__init__(self, "VPP", name, *poolNames)
		self.basePoints = pool
		self.control = control
		samplePools = []
	#methods for easy adding sample pools to the VPP class
	def addSamplePool(self, name):
		samplePools.append(SampleVPP(name, self.basePoints, self.control))
	def removeSamplePool(self, samplePoolName):
		count = 0
		for samplePool in samplePools:
			if(samplePool.name == samplePoolName):
				samplePools.pop(count)
			count += 1
#class for sample pools that will be aggregated by the VPP class
class SampleVPP:
	def __init__(self, name, pool, control):
		self.name = name
		self.pool = pool
		self.control = control
		powers = []
	#methods for easy adding powers to the SampleVPP class
	def addPower(self, Power):
		self.powers.append(Power)
	def removePower(self, powerName):
		count = 0
		for power in powers:
			if(power.name == powerName):
				powers.pop(count)
			count += 1	


#Test that makes a trait with type Power, name Test, and two point pools named george and bob			
testTrait = Trait('Perk', 'Test', 'george', 'bob')
print(testTrait.name)
print(testTrait.basePointPoolNames[0])
print(" ")
#Testing a subclass of trait to make sure it inherits properly
testPower = Power('Power', 'TestPower', True, 5, 'georgio', 'bob')
print(testPower.name)
print(testPower.basePointPoolNames[0])