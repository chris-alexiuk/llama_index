from llama_index.extractors.metadata_extractors import (
    BaseExtractor,
    SummaryExtractor,
    QuestionsAnsweredExtractor,
    EntityExtractor,
    TitleExtractor,
    KeywordExtractor,
)


def load_extractor(
    data: dict,
) -> BaseExtractor:
    extractor_name = data.get("class_name", None)
    if extractor_name is None:
        raise ValueError("Extractor loading requires a class_name")

    if extractor_name == SummaryExtractor.class_name():
        return SummaryExtractor.from_dict(data)
    elif extractor_name == QuestionsAnsweredExtractor.class_name():
        return QuestionsAnsweredExtractor.from_dict(data)
    elif extractor_name == EntityExtractor.class_name():
        return EntityExtractor.from_dict(data)
    elif extractor_name == TitleExtractor.class_name():
        return TitleExtractor.from_dict(data)
    elif extractor_name == KeywordExtractor.class_name():
        return KeywordExtractor.from_dict(data)
    else:
        raise ValueError(f"Unknown extractor name: {extractor_name}")
