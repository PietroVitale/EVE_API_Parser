class char_ChatChannels:
	def __init__(self):

		self.channels = []

		class channels:
			def __init__(self, key, params):
			#params = [ownerID,ownerName,displayName,comparisonKey]
				self.key = key
				self.ownerID = param[1]
				self.ownerName = param[2]
				self.displayName = param[3]
				self.comparisonKey = param[4]
				self.hasPassword = param[5]
				self.motd = param[6]
		
class char_Bookmarks:
	def __init__(self):

		self.folders = []

		class folders:
			def __init__(self, key, params):
			#params = []
				self.key = key
				self.folderName = param[1]
		
				self.bookmarks = []

				class bookmarks:
					def __init__(self, key, params):
					#params = [creatorID,created,itemID,typeID,locationID,x,y,z]
						self.key = key
						self.creatorID = param[1]
						self.created = param[2]
						self.itemID = param[3]
						self.typeID = param[4]
						self.locationID = param[5]
						self.x = param[6]
						self.y = param[7]
						self.z = param[8]
						self.memo = param[9]
						self.note = param[10]
				
class char_AssetList:
	def __init__(self):

		self.assets = []

		class assets:
			def __init__(self, key, params):
			#params = [locationID,typeID,quantity]
				self.key = key
				self.locationID = param[1]
				self.typeID = param[2]
				self.quantity = param[3]
				self.flag = param[4]
				self.singleton = param[5]
		
				self.contents = []

				class contents:
					def __init__(self, key, params):
					#params = [typeID,quantity]
						self.key = key
						self.typeID = param[1]
						self.quantity = param[2]
						self.flag = param[3]
						self.singleton = param[4]
				
class char_Contracts:
	def __init__(self):

		self.contractList = []

		class contractList:
			def __init__(self, key, params):
			#params = [issuerID,issuerCorpID,assigneeID,acceptorID,startStationID,endStationID,type,status,title,forCorp,availability,dateIssued,dateExpired,dateAccepted,numDays,dateCompleted,price,reward,collateral]
				self.key = key
				self.issuerID = param[1]
				self.issuerCorpID = param[2]
				self.assigneeID = param[3]
				self.acceptorID = param[4]
				self.startStationID = param[5]
				self.endStationID = param[6]
				self.type = param[7]
				self.status = param[8]
				self.title = param[9]
				self.forCorp = param[10]
				self.availability = param[11]
				self.dateIssued = param[12]
				self.dateExpired = param[13]
				self.dateAccepted = param[14]
				self.numDays = param[15]
				self.dateCompleted = param[16]
				self.price = param[17]
				self.reward = param[18]
				self.collateral = param[19]
				self.buyout = param[20]
				self.volume = param[21]
		
class account_AccountStatus:
	def __init__(self):

		self.multiCharacterTraining = []

		class multiCharacterTraining:
			def __init__(self, key, params):
			#params = []
				self.key = key
		
class char_AccountBalance:
	def __init__(self):

		self.accounts = []

		class accounts:
			def __init__(self, key, params):
			#params = []
				self.key = key
				self.accountKey = param[1]
				self.balance = param[2]
		
class char_AccountBalance:
	def __init__(self):

		self.accounts = []

		class accounts:
			def __init__(self, key, params):
			#params = []
				self.key = key
				self.accountKey = param[1]
				self.balance = param[2]
		
class char_WalletTransactions:
	def __init__(self):

		self.transactions = []

		class transactions:
			def __init__(self, key, params):
			#params = [transactionID,quantity,typeName,typeID,price,clientID,clientName,stationID,stationName,transactionType,transactionFor]
				self.key = key
				self.transactionID = param[1]
				self.quantity = param[2]
				self.typeName = param[3]
				self.typeID = param[4]
				self.price = param[5]
				self.clientID = param[6]
				self.clientName = param[7]
				self.stationID = param[8]
				self.stationName = param[9]
				self.transactionType = param[10]
				self.transactionFor = param[11]
				self.journalTransactionID = param[12]
				self.clientTypeID = param[13]
		
class char_WalletJournal:
	def __init__(self):

		self.transactions = []

		class transactions:
			def __init__(self, key, params):
			#params = [refID,refTypeID,ownerName1,ownerID1,ownerName2,ownerID2,argName1,argID1,amount,balance,reason,taxReceiverID,taxAmount]
				self.key = key
				self.refID = param[1]
				self.refTypeID = param[2]
				self.ownerName1 = param[3]
				self.ownerID1 = param[4]
				self.ownerName2 = param[5]
				self.ownerID2 = param[6]
				self.argName1 = param[7]
				self.argID1 = param[8]
				self.amount = param[9]
				self.balance = param[10]
				self.reason = param[11]
				self.taxReceiverID = param[12]
				self.taxAmount = param[13]
				self.owner1TypeID = param[14]
				self.owner2TypeID = param[15]
		
class char_UpcomingCalendarEvents:
	def __init__(self):

		self.upcomingEvents = []

		class upcomingEvents:
			def __init__(self, key, params):
			#params = [ownerID,ownerName,eventDate,eventTitle,duration,importance,response]
				self.key = key
				self.ownerID = param[1]
				self.ownerName = param[2]
				self.eventDate = param[3]
				self.eventTitle = param[4]
				self.duration = param[5]
				self.importance = param[6]
				self.response = param[7]
				self.eventText = param[8]
				self.ownerTypeID = param[9]
		
class char_Standings:
	def __init__(self):

				self.agents = []

				class agents:
					def __init__(self, key, params):
					#params = []
						self.key = key
						self.fromName = param[1]
						self.standing = param[2]
				
				self.NPCCorporations = []

				class NPCCorporations:
					def __init__(self, key, params):
					#params = []
						self.key = key
						self.fromName = param[1]
						self.standing = param[2]
				
				self.factions = []

				class factions:
					def __init__(self, key, params):
					#params = []
						self.key = key
						self.fromName = param[1]
						self.standing = param[2]
				
class char_SkillQueue:
	def __init__(self):

		self.skillqueue = []

		class skillqueue:
			def __init__(self, key, params):
			#params = [typeID,level,startSP,endSP]
				self.key = key
				self.typeID = param[1]
				self.level = param[2]
				self.startSP = param[3]
				self.endSP = param[4]
				self.startTime = param[5]
				self.endTime = param[6]
		
class char_SkillInTraining:
	def __init__(self):

class char_Research:
	def __init__(self):

		self.research = []

		class research:
			def __init__(self, key, params):
			#params = [skillTypeID,researchStartDate]
				self.key = key
				self.skillTypeID = param[1]
				self.researchStartDate = param[2]
				self.pointsPerDay = param[3]
				self.remainderPoints = param[4]
		
class char_Notifications:
	def __init__(self):

		self.notifications = []

		class notifications:
			def __init__(self, key, params):
			#params = [typeID,senderID,senderName]
				self.key = key
				self.typeID = param[1]
				self.senderID = param[2]
				self.senderName = param[3]
				self.sentDate = param[4]
				self.read = param[5]
		
class char_Medals:
	def __init__(self):

		self.currentCorporation = []

		class currentCorporation:
			def __init__(self, key, params):
			#params = [reason,status]
				self.key = key
				self.reason = param[1]
				self.status = param[2]
				self.issuerID = param[3]
				self.issued = param[4]
		
		self.otherCorporations = []

		class otherCorporations:
			def __init__(self, key, params):
			#params = [reason,status,issuerID,issued,corporationID]
				self.key = key
				self.reason = param[1]
				self.status = param[2]
				self.issuerID = param[3]
				self.issued = param[4]
				self.corporationID = param[5]
				self.title = param[6]
				self.description = param[7]
		
class char_MarketOrders:
	def __init__(self):

		self.orders = []

		class orders:
			def __init__(self, key, params):
			#params = [charID,stationID,volEntered,volRemaining,minVolume,orderState,typeID,range,accountKey,duration,escrow,price]
				self.key = key
				self.charID = param[1]
				self.stationID = param[2]
				self.volEntered = param[3]
				self.volRemaining = param[4]
				self.minVolume = param[5]
				self.orderState = param[6]
				self.typeID = param[7]
				self.range = param[8]
				self.accountKey = param[9]
				self.duration = param[10]
				self.escrow = param[11]
				self.price = param[12]
				self.bid = param[13]
				self.issued = param[14]
		
class char_MailMessages:
	def __init__(self):

		self.messages = []

		class messages:
			def __init__(self, key, params):
			#params = [senderID,senderName,sentDate,title,toCorpOrAllianceID]
				self.key = key
				self.senderID = param[1]
				self.senderName = param[2]
				self.sentDate = param[3]
				self.title = param[4]
				self.toCorpOrAllianceID = param[5]
				self.toCharacterIDs = param[6]
				self.toListID = param[7]
		
class char_MailingLists:
	def __init__(self):

		self.mailingLists = []

		class mailingLists:
			def __init__(self, key, params):
			#params = []
				self.key = key
				self.displayName = param[1]
		
class char_IndustryJobs:
	def __init__(self):

		self.jobs = []

		class jobs:
			def __init__(self, key, params):
			#params = [installerID,installerName,facilityID,solarSystemID,solarSystemName,stationID,activityID,blueprintID,blueprintTypeID,blueprintTypeName,blueprintLocationID,outputLocationID,runs,cost,teamID,licensedRuns,probability,productTypeID,productTypeName,status,timeInSeconds,startDate,endDate,pauseDate,completedDate]
				self.key = key
				self.installerID = param[1]
				self.installerName = param[2]
				self.facilityID = param[3]
				self.solarSystemID = param[4]
				self.solarSystemName = param[5]
				self.stationID = param[6]
				self.activityID = param[7]
				self.blueprintID = param[8]
				self.blueprintTypeID = param[9]
				self.blueprintTypeName = param[10]
				self.blueprintLocationID = param[11]
				self.outputLocationID = param[12]
				self.runs = param[13]
				self.cost = param[14]
				self.teamID = param[15]
				self.licensedRuns = param[16]
				self.probability = param[17]
				self.productTypeID = param[18]
				self.productTypeName = param[19]
				self.status = param[20]
				self.timeInSeconds = param[21]
				self.startDate = param[22]
				self.endDate = param[23]
				self.pauseDate = param[24]
				self.completedDate = param[25]
				self.completedCharacterID = param[26]
				self.successfulRuns = param[27]
		
class char_ContactNotifications:
	def __init__(self):

		self.contactNotifications = []

		class contactNotifications:
			def __init__(self, key, params):
			#params = [senderID,senderName]
				self.key = key
				self.senderID = param[1]
				self.senderName = param[2]
				self.sentDate = param[3]
				self.messageData = param[4]
		
class char_ContactList:
	def __init__(self):

		self.contactList = []

		class contactList:
			def __init__(self, key, params):
			#params = [contactName,standing,contactTypeID]
				self.key = key
				self.contactName = param[1]
				self.standing = param[2]
				self.contactTypeID = param[3]
				self.labelMask = param[4]
				self.inWatchlist = param[5]
		
		self.contactLabels = []

		class contactLabels:
			def __init__(self, key, params):
			#params = []
				self.key = key
				self.name = param[1]
		
		self.corporateContactList = []

		class corporateContactList:
			def __init__(self, key, params):
			#params = [contactName,standing]
				self.key = key
				self.contactName = param[1]
				self.standing = param[2]
				self.contactTypeID = param[3]
				self.labelMask = param[4]
		
		self.corporateContactLabels = []

		class corporateContactLabels:
			def __init__(self, key, params):
			#params = []
				self.key = key
				self.name = param[1]
		
		self.allianceContactList = []

		class allianceContactList:
			def __init__(self, key, params):
			#params = [contactName,standing]
				self.key = key
				self.contactName = param[1]
				self.standing = param[2]
				self.contactTypeID = param[3]
				self.labelMask = param[4]
		
		self.allianceContactLabels = []

		class allianceContactLabels:
			def __init__(self, key, params):
			#params = []
				self.key = key
				self.name = param[1]
		
class char_CharacterSheet:
	def __init__(self):

		self.jumpClones = []

		class jumpClones:
			def __init__(self, key, params):
			#params = [typeID]
				self.key = key
				self.typeID = param[1]
				self.locationID = param[2]
				self.cloneName = param[3]
		
		self.jumpCloneImplants = []

		class jumpCloneImplants:
			def __init__(self, key, params):
			#params = []
				self.key = key
				self.typeID = param[1]
				self.typeName = param[2]
		
		self.implants = []

		class implants:
			def __init__(self, key, params):
			#params = []
				self.key = key
				self.typeName = param[1]
		
		self.skills = []

		class skills:
			def __init__(self, key, params):
			#params = [skillpoints]
				self.key = key
				self.skillpoints = param[1]
				self.level = param[2]
				self.published = param[3]
		
		self.certificates = []

		class certificates:
			def __init__(self, key, params):
			#params = []
				self.key = key
		
		self.corporationRoles = []

		class corporationRoles:
			def __init__(self, key, params):
			#params = []
				self.key = key
				self.roleName = param[1]
		
		self.corporationRolesAtHQ = []

		class corporationRolesAtHQ:
			def __init__(self, key, params):
			#params = []
				self.key = key
				self.roleName = param[1]
		
		self.corporationRolesAtBase = []

		class corporationRolesAtBase:
			def __init__(self, key, params):
			#params = []
				self.key = key
				self.roleName = param[1]
		
		self.corporationRolesAtOther = []

		class corporationRolesAtOther:
			def __init__(self, key, params):
			#params = []
				self.key = key
				self.roleName = param[1]
		
		self.corporationTitles = []

		class corporationTitles:
			def __init__(self, key, params):
			#params = []
				self.key = key
				self.titleName = param[1]
		
class char_AssetList:
	def __init__(self):

		self.assets = []

		class assets:
			def __init__(self, key, params):
			#params = [locationID,typeID,quantity]
				self.key = key
				self.locationID = param[1]
				self.typeID = param[2]
				self.quantity = param[3]
				self.flag = param[4]
				self.singleton = param[5]
		
				self.contents = []

				class contents:
					def __init__(self, key, params):
					#params = [typeID,quantity]
						self.key = key
						self.typeID = param[1]
						self.quantity = param[2]
						self.flag = param[3]
						self.singleton = param[4]
				
class char_AccountBalance:
	def __init__(self):

		self.accounts = []

		class accounts:
			def __init__(self, key, params):
			#params = []
				self.key = key
				self.accountKey = param[1]
				self.balance = param[2]
		
class corp_Bookmarks:
	def __init__(self):

		self.folders = []

		class folders:
			def __init__(self, key, params):
			#params = []
				self.key = key
				self.folderName = param[1]
				self.creatorID = param[2]
		
				self.bookmarks = []

				class bookmarks:
					def __init__(self, key, params):
					#params = [creatorID,created,itemID,typeID,locationID,x,y,z]
						self.key = key
						self.creatorID = param[1]
						self.created = param[2]
						self.itemID = param[3]
						self.typeID = param[4]
						self.locationID = param[5]
						self.x = param[6]
						self.y = param[7]
						self.z = param[8]
						self.memo = param[9]
						self.note = param[10]
				
class corp_AssetList:
	def __init__(self):

		self.assets = []

		class assets:
			def __init__(self, key, params):
			#params = [locationID,typeID,quantity]
				self.key = key
				self.locationID = param[1]
				self.typeID = param[2]
				self.quantity = param[3]
				self.flag = param[4]
				self.singleton = param[5]
		
class corp_Contracts:
	def __init__(self):

		self.contractList = []

		class contractList:
			def __init__(self, key, params):
			#params = [issuerID,issuerCorpID,assigneeID,acceptorID,startStationID,endStationID,type,status,title,forCorp,availability,dateIssued,dateExpired,dateAccepted,numDays,dateCompleted,price,reward,collateral]
				self.key = key
				self.issuerID = param[1]
				self.issuerCorpID = param[2]
				self.assigneeID = param[3]
				self.acceptorID = param[4]
				self.startStationID = param[5]
				self.endStationID = param[6]
				self.type = param[7]
				self.status = param[8]
				self.title = param[9]
				self.forCorp = param[10]
				self.availability = param[11]
				self.dateIssued = param[12]
				self.dateExpired = param[13]
				self.dateAccepted = param[14]
				self.numDays = param[15]
				self.dateCompleted = param[16]
				self.price = param[17]
				self.reward = param[18]
				self.collateral = param[19]
				self.buyout = param[20]
				self.volume = param[21]
		
class corp_Titles:
	def __init__(self):

		self.titles = []

		class titles:
			def __init__(self, key, params):
			#params = []
				self.key = key
				self.titleName = param[1]
		
class corp_WalletTransactions:
	def __init__(self):

		self.transactions = []

		class transactions:
			def __init__(self, key, params):
			#params = [transactionID,quantity,typeName,typeID,price,clientID,clientName,characterID,characterName,stationID,stationName,transactionType,transactionFor]
				self.key = key
				self.transactionID = param[1]
				self.quantity = param[2]
				self.typeName = param[3]
				self.typeID = param[4]
				self.price = param[5]
				self.clientID = param[6]
				self.clientName = param[7]
				self.characterID = param[8]
				self.characterName = param[9]
				self.stationID = param[10]
				self.stationName = param[11]
				self.transactionType = param[12]
				self.transactionFor = param[13]
				self.journalTransactionID = param[14]
				self.clientTypeID = param[15]
		
class corp_WalletJournal:
	def __init__(self):

		self.entries = []

		class entries:
			def __init__(self, key, params):
			#params = [refID,refTypeID,ownerName1,ownerID1,ownerName2,ownerID2,argName1,argID1,amount,balance,reason]
				self.key = key
				self.refID = param[1]
				self.refTypeID = param[2]
				self.ownerName1 = param[3]
				self.ownerID1 = param[4]
				self.ownerName2 = param[5]
				self.ownerID2 = param[6]
				self.argName1 = param[7]
				self.argID1 = param[8]
				self.amount = param[9]
				self.balance = param[10]
				self.reason = param[11]
				self.owner1TypeID = param[12]
				self.owner2TypeID = param[13]
		
class corp_StarbaseList:
	def __init__(self):

		self.starbases = []

		class starbases:
			def __init__(self, key, params):
			#params = [typeID,locationID,moonID,state,stateTimestamp]
				self.key = key
				self.typeID = param[1]
				self.locationID = param[2]
				self.moonID = param[3]
				self.state = param[4]
				self.stateTimestamp = param[5]
				self.onlineTimestamp = param[6]
				self.standingOwnerID = param[7]
		
class corp_Standings:
	def __init__(self):

				self.agents = []

				class agents:
					def __init__(self, key, params):
					#params = []
						self.key = key
						self.fromName = param[1]
						self.standing = param[2]
				
				self.NPCCorporations = []

				class NPCCorporations:
					def __init__(self, key, params):
					#params = []
						self.key = key
						self.fromName = param[1]
						self.standing = param[2]
				
				self.factions = []

				class factions:
					def __init__(self, key, params):
					#params = []
						self.key = key
						self.fromName = param[1]
						self.standing = param[2]
				
class corp_Shareholders:
	def __init__(self):

		self.characters = []

		class characters:
			def __init__(self, key, params):
			#params = [shareholderName,shareholderCorporationID]
				self.key = key
				self.shareholderName = param[1]
				self.shareholderCorporationID = param[2]
				self.shareholderCorporationName = param[3]
				self.shares = param[4]
		
		self.corporations = []

		class corporations:
			def __init__(self, key, params):
			#params = []
				self.key = key
				self.shareholderName = param[1]
				self.shares = param[2]
		
class corp_OutpostServiceDetail:
	def __init__(self):

		self.outpostServiceDetails = []

		class outpostServiceDetails:
			def __init__(self, key, params):
			#params = [ownerID,serviceName,minStanding]
				self.key = key
				self.ownerID = param[1]
				self.serviceName = param[2]
				self.minStanding = param[3]
				self.surchargePerBadStanding = param[4]
				self.discountPerGoodStanding = param[5]
		
class corp_OutpostList:
	def __init__(self):

		self.corporationStarbases = []

		class corporationStarbases:
			def __init__(self, key, params):
			#params = [ownerID,stationName,solarSystemID,dockingCostPerShipVolume,officeRentalCost,stationTypeID,reprocessingEfficiency,reprocessingStationTake,standingOwnerID,x]
				self.key = key
				self.ownerID = param[1]
				self.stationName = param[2]
				self.solarSystemID = param[3]
				self.dockingCostPerShipVolume = param[4]
				self.officeRentalCost = param[5]
				self.stationTypeID = param[6]
				self.reprocessingEfficiency = param[7]
				self.reprocessingStationTake = param[8]
				self.standingOwnerID = param[9]
				self.x = param[10]
				self.y = param[11]
				self.z = param[12]
		
class corp_Medals:
	def __init__(self):

		self.medals = []

		class medals:
			def __init__(self, key, params):
			#params = [title,description]
				self.key = key
				self.title = param[1]
				self.description = param[2]
				self.creatorID = param[3]
				self.created = param[4]
		
class corp_MarketOrders:
	def __init__(self):

		self.orders = []

		class orders:
			def __init__(self, key, params):
			#params = [charID,stationID,volEntered,volRemaining,minVolume,orderState,typeID,range,accountKey,duration,escrow,price]
				self.key = key
				self.charID = param[1]
				self.stationID = param[2]
				self.volEntered = param[3]
				self.volRemaining = param[4]
				self.minVolume = param[5]
				self.orderState = param[6]
				self.typeID = param[7]
				self.range = param[8]
				self.accountKey = param[9]
				self.duration = param[10]
				self.escrow = param[11]
				self.price = param[12]
				self.bid = param[13]
				self.issued = param[14]
		
class corp_MemberSecurityLog:
	def __init__(self):

		self.roleHistory = []

		class roleHistory:
			def __init__(self, key, params):
			#params = [characterID]
				self.key = key
				self.characterID = param[1]
				self.issuerID = param[2]
				self.roleLocationType = param[3]
		
class corp_MemberSecurity:
	def __init__(self):

		self.members = []

		class members:
			def __init__(self, key, params):
			#params = []
				self.key = key
				self.name = param[1]
		
				self.roles = []

				class roles:
					def __init__(self, key, params):
					#params = []
						self.key = key
						self.roleName = param[1]
				
				self.grantableRoles = []

				class grantableRoles:
					def __init__(self, key, params):
					#params = []
						self.key = key
						self.roleName = param[1]
				
				self.rolesAtHQ = []

				class rolesAtHQ:
					def __init__(self, key, params):
					#params = []
						self.key = key
						self.roleName = param[1]
				
				self.grantableRolesAtHQ = []

				class grantableRolesAtHQ:
					def __init__(self, key, params):
					#params = []
						self.key = key
						self.roleName = param[1]
				
				self.rolesAtBase = []

				class rolesAtBase:
					def __init__(self, key, params):
					#params = []
						self.key = key
						self.roleName = param[1]
				
				self.grantableRolesAtBase = []

				class grantableRolesAtBase:
					def __init__(self, key, params):
					#params = []
						self.key = key
						self.roleName = param[1]
				
				self.rolesAtOther = []

				class rolesAtOther:
					def __init__(self, key, params):
					#params = []
						self.key = key
						self.roleName = param[1]
				
				self.grantableRolesAtOther = []

				class grantableRolesAtOther:
					def __init__(self, key, params):
					#params = []
						self.key = key
						self.roleName = param[1]
				
				self.titles = []

				class titles:
					def __init__(self, key, params):
					#params = []
						self.key = key
						self.titleName = param[1]
				
class corp_IndustryJobs:
	def __init__(self):

		self.jobs = []

		class jobs:
			def __init__(self, key, params):
			#params = [installerID,installerName,facilityID,solarSystemID,solarSystemName,stationID,activityID,blueprintID,blueprintTypeID,blueprintTypeName,blueprintLocationID,outputLocationID,runs,cost,teamID,licensedRuns,probability,productTypeID,productTypeName,status,timeInSeconds,startDate,endDate,pauseDate,completedDate]
				self.key = key
				self.installerID = param[1]
				self.installerName = param[2]
				self.facilityID = param[3]
				self.solarSystemID = param[4]
				self.solarSystemName = param[5]
				self.stationID = param[6]
				self.activityID = param[7]
				self.blueprintID = param[8]
				self.blueprintTypeID = param[9]
				self.blueprintTypeName = param[10]
				self.blueprintLocationID = param[11]
				self.outputLocationID = param[12]
				self.runs = param[13]
				self.cost = param[14]
				self.teamID = param[15]
				self.licensedRuns = param[16]
				self.probability = param[17]
				self.productTypeID = param[18]
				self.productTypeName = param[19]
				self.status = param[20]
				self.timeInSeconds = param[21]
				self.startDate = param[22]
				self.endDate = param[23]
				self.pauseDate = param[24]
				self.completedDate = param[25]
				self.completedCharacterID = param[26]
				self.successfulRuns = param[27]
		
class corp_ContainerLog:
	def __init__(self):

		self.containerLog = []

		class containerLog:
			def __init__(self, key, params):
			#params = [itemID,itemTypeID,actorID,actorName,flag,locationID,action,passwordType,typeID,quantity]
				self.key = key
				self.itemID = param[1]
				self.itemTypeID = param[2]
				self.actorID = param[3]
				self.actorName = param[4]
				self.flag = param[5]
				self.locationID = param[6]
				self.action = param[7]
				self.passwordType = param[8]
				self.typeID = param[9]
				self.quantity = param[10]
				self.oldConfiguration = param[11]
				self.newConfiguration = param[12]
		
class corp_ContactList:
	def __init__(self):

		self.corporateContactList = []

		class corporateContactList:
			def __init__(self, key, params):
			#params = [contactName,standing]
				self.key = key
				self.contactName = param[1]
				self.standing = param[2]
				self.contactTypeID = param[3]
				self.labelMask = param[4]
		
		self.corporateContactLabels = []

		class corporateContactLabels:
			def __init__(self, key, params):
			#params = []
				self.key = key
				self.name = param[1]
		
		self.allianceContactList = []

		class allianceContactList:
			def __init__(self, key, params):
			#params = [contactName,standing]
				self.key = key
				self.contactName = param[1]
				self.standing = param[2]
				self.contactTypeID = param[3]
				self.labelMask = param[4]
		
		self.allianceContactLabels = []

		class allianceContactLabels:
			def __init__(self, key, params):
			#params = []
				self.key = key
				self.name = param[1]
		
class corp_CorporationSheet:
	def __init__(self):

		self.divisions = []

		class divisions:
			def __init__(self, key, params):
			#params = []
				self.key = key
				self.description = param[1]
		
		self.walletDivisions = []

		class walletDivisions:
			def __init__(self, key, params):
			#params = []
				self.key = key
				self.description = param[1]
		
class corp_MemberMedals:
	def __init__(self):

		self.issuedMedals = []

		class issuedMedals:
			def __init__(self, key, params):
			#params = [characterID,reason,status]
				self.key = key
				self.characterID = param[1]
				self.reason = param[2]
				self.status = param[3]
				self.issuerID = param[4]
				self.issued = param[5]
		
class corp_AssetList:
	def __init__(self):

		self.assets = []

		class assets:
			def __init__(self, key, params):
			#params = [locationID,typeID,quantity]
				self.key = key
				self.locationID = param[1]
				self.typeID = param[2]
				self.quantity = param[3]
				self.flag = param[4]
				self.singleton = param[5]
		
class corp_AccountBalance:
	def __init__(self):

		self.accounts = []

		class accounts:
			def __init__(self, key, params):
			#params = []
				self.key = key
				self.accountKey = param[1]
				self.balance = param[2]
		
