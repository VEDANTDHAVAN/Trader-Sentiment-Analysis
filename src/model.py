from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

def train_model(df):
    data = df.copy()
    enc = LabelEncoder()

    data["Classification"] = enc.fit_transform(
        data["Classification"]
    )

    data["Coin"] = enc.fit_transform(data["Coin"])

    data["Side"] = enc.fit_transform(data["Side"])

    data["Direction"] = enc.fit_transform(
        data["Direction"]
    )

    features = [
        "Classification", "Size USD", "Fee",
        "Coin", "Side", "Direction"
    ]

    X = data[features]

    y = data["win"]

    X_train, X_test, y_train, y_test = (
        train_test_split(
            X, y,
            test_size=0.2,
            random_state=42
        )
    )

    model = RandomForestClassifier(
        n_estimators=200,
        random_state=42
    )

    model.fit(
        X_train,
        y_train
    )

    preds = model.predict(
        X_test
    )

    print(
        classification_report(
            y_test,
            preds
        )
    )

    return model