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
class Trait:
	def __init__(self, type, name):
		self.type = type
		self.name = name
		modifiers = []
		basePoints = 0
		modFlatPoints = 0
		advTotal = 0
		limTotal = 0
		activePoints = (basePoints+modFlatPoints)*(1+advTotal)
		totalPoints = activePoints/(1+limTotal)
	def addMod(self, Modifier):
		self.modifiers.append(Modifier)
	def removeMod(self, modName):
		count = 0
		for mod in modifiers:
			if(mod.name == modName):
				modifiers.pop(count)
			count += 1
class Modifier:
	def __init__(self, id, type, value):
		self.name = name
		self.type = type
		self.value = value
class Characteristc(Trait):
	def __init__(self, type, name, rollChar):
		Trait.__init__(self, type, name)
		self.rollChar = rollChar
		roll = 9
class Skill(Trait):
	def __init__(self, type, name, char, rollSkill):
		Trait.__init__(self, type, name)
		self.char = char
		self.rollSkill = rollSkill
		roll = 8
		basePoints = 1
class KPSSkill(Skill):
	def __init__(self, type, name, char, kps, field):
		Skill.__init__(self, type, name, char, True)
		self.kps = kps
		self.field = field
		self.elevenRoll = False
class Power(Trait):
	def __init__(self, type, name, d6Power, costPerD6):
		Trait.__init__(self, type, name)
		self.d6Power = d6Power
		self.costPerD6 = costPerD6
class MPPower(Power):
	def __init__(self, type, name, d6Power, costPerD6, fixed):
		Power.__init__(self, type, name, d6Power, costPerD6)
		self.fixed = fixed
class Multipower(Trait):
	def __init__(self, type, name):
		Trait.__init__(self, type, name)
		powers = []
		totalPowersCost = 0
	def addPower(self, MPPower):
		self.powers.append(MPPower)
	def removePower(self, powerName):
		count = 0
		for power in powers:
			if(power.name == powerName):
				powers.pop(count)
			count += 1
class VPP(Trait):
	def __init__(self, type, name, pool, control):
		Trait.__init__(self, type, name)
		self.basePoints = pool
		self.control = control
		samplePools = []
	def addSamplePool(self, name):
		samplePools.append(SampleVPP(name, self.basePoints, self.control))
	def removeSamplePool(self, samplePoolName):
		count = 0
		for samplePool in samplePools:
			if(samplePool.name == samplePoolName):
				samplePools.pop(count)
			count += 1
class SampleVPP:
	def __init__(self, name, pool, control):
		self.name = name
		self.pool = pool
		self.control = control
		powers = []
	def addPower(self, Power):
		self.powers.append(Power)
	def removePower(self, powerName):
		count = 0
		for power in powers:
			if(power.name == powerName):
				powers.pop(count)
			count += 1
