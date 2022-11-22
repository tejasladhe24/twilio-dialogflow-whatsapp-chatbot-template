class WADMapper:
    session = None
    query_input = None
    context = None
    response = None

    def setResponse(self, res):
        self.response = res

    def setSession(self, session):
        self.session = session

    def setQuery(self, query):
        self.query_input = query

    def setContext(self, context):
        self.context = context
