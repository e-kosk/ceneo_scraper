class Opinion:

    def __init__(self, opinion_id, author, recommendation, stars, content, cons, pros, useful, useless, opinion_date, purchase_date):
        self.opinion_id = opinion_id
        self.author = author
        self.recommendation = recommendation
        self.stars = stars
        self.content = content
        self.cons = cons
        self.pros = pros
        self.useful = useful
        self.useless = useless
        self.opinion_date = opinion_date
        self.purchase_date = purchase_date

    def __str__(self):
        return f'({self.opinion_id}) {self.author}: {self.content[:100]}'

    def __repr__(self):
        return f'Opinion({self.opinion_id}, {self.author}, {self.author}, {self.recommendation}, {self.stars}, {self.content}, {self.cons}, {self.pros}, {self.useful}, {self.useless}, {self.opinion_date}, {self.purchase_date}'
