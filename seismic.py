class SeismicProcessor():
    def __init__(self, dataframe):
        self.data = dataframe

    def get_years(self):
        years_series = list(self.data['Year'].unique())
        years = []
        for y in years_series:
            years.append(str(y))
        return years

    def list_events_by_year(self, year):
        filtered_data = self.data.loc[self.data['Year'] == year]
        filtered_data_dict = filtered_data.T.to_dict().values()
        filtered_data_dict = list(filtered_data_dict)
        return filtered_data_dict
