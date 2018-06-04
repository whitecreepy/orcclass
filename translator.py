
class Translator:
    features_names = [
        "Высококвалифицированные инженерные и научные кадры",
        "Молодые специалисты",
        "Публикационная активность",
        "Качество патентов",
        "Изменение проектных решений",
        "Выполнение Бизнес-плана"
    ]

    features_values = [
        [
            "Недостаточное количество высококвалифицированных инженерных и научных кадров.",
            "Достаточное количество высококвалифицированных инженерных и научных кадров, "
            "годовой план по обучению сотрудников не выполнен.",
            "Достаточное количество высококвалифицированных инженерных и "
            "научных кадров, выполнен годовой план по обучению сотрудников.",
        ],
        [
            "Программы по привлечению, удержанию МС и развитию их компетенций не проводятся.",
            "Число МС менее 5%, проводятся программы по привлечению, удержанию МС и развитию их компетенций.",
            "Число молодых специалистов (МС) не менее 5%, проводятся программы по привлечению, "
            "удержанию МС и развитию их компетенций.",
        ],
        [
            "Статьи сотрудников института, опубликованные в журналах, входящих в список "
            "Scopus/ВАК, не имеют теоретической и практической ценности или отсутствуют.",
            "Статьи сотрудников института, опубликованные в журналах, входящих в список "
            "Scopus/ВАК, и имеют некоторую теоретическую и/или практическую ценность.",
            "Статьи сотрудников института, опубликованные в журналах, входящих в "
            "список Scopus/ВАК, и имеют высокую теоретическую и/или практическую ценность.",
        ],
        [
            "Зарегистрированные в течение года патенты не имеют практической ценности "
            "для Компании или отсутсутствуют.",
            "Зарегистрированные в течение года патенты имеют некоторую практическую "
            "ценность для Компании.",
            "Зарегистрированные в течение года патенты имеют высокую практическую "
            "ценность для Компании.",
        ],
        [
            "По результатам Главгосэкспертизы проектные мощности объектов строительства "
            "изменились более чем 50% объектам обустройства месторождения или сроки "
            "строительства сдвинуты более чем на 6 месяцев.",
            "По результатам Главгосэкспертизы проектные мощности объектов строительства "
            "изменились не более чем 50% объектам обустройства месторождения или сроки "
            "строительства сдвинуты менее чем на 6 месяцев.",
            "По результатам Главгосэкспертизы проектные решения не менялись.",
        ],
        [
            "Бизнес-план не выполнен.",
            "Бизнес-план выполнен более чем на 80%.",
            "Бизнес-план выполнен на 100% или перевыполнен.",
        ]
    ]

    def __init__(self, size=6):
        if size > 6:
            raise ValueError("Not supported")
        self._size = size

    def get_feature(self, dimension):
        return self.features_names[dimension]

    def translate(self, vector):
        result = []
        for i in range(len(vector)):
            result.append(str(i + 1) + ". " + self.features_values[i][vector[i]])
        return result


if __name__ == '__main__':
    translator = Translator()
    print(translator.translate([1, 1, 1, 1, 1, 1]))
