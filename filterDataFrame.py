import pandas
class filterDataFrame:

	###!!!!Different filter methods to come!!!!

	def __init__(self, df):
		self.df = df

	def sortByNumberOfEpisodes(self, highest=None, lowest=0, exact=None):
		newFrame = pandas.DataFrame()
		if exact != None:
			for index, row in self.df.iterrows():
				if row['Number of Episodes'] == exact:
					df2 = {'Title':row['Title'], 'URL':row['URL'], 'Number of Episodes':row['Number of Episodes'], 'Status':row['Status']}
					newFrame = newFrame.append(df2, ignore_index = True)
			return newFrame
		elif highest != None:
			for i in range(lowest, (highest + 1)):
				for index, row in self.df.iterrows():
					if row['Number of Episodes'] == i:
						df2 = {'Title':row['Title'], 'URL':row['URL'], 'Number of Episodes':row['Number of Episodes'], 'Status':row['Status']}
						newFrame = newFrame.append(df2, ignore_index = True)
			return newFrame
		else:
			raise Exception('Required paramaters in self.sortByNumberOfEpisodes() are missing')

if __name__ == "__main__":
	filterer = filterDataFrame(pandas.read_csv('shows.csv'))
	print(filterer.sortByNumberOfEpisodes(lowest=16, highest=16))
