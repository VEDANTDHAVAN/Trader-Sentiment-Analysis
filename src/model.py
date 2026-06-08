from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pandas as pd
import matplotlib.pyplot as plt

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

    # Added feature importance reporting.
    # Reason: A research project should explain WHY predictions happen, not just report accuracy.
    importance = pd.DataFrame({
        "Feature": features, 
        "Importance": model.feature_importances_
    })

    importance = (
        importance.sort_values(
            "Importance", ascending=False
        )
    )

    # Feature Importance
    importance = pd.DataFrame({
        "Feature": features,
        "Importance": model.feature_importances_
    })

    importance = importance.sort_values(
        by="Importance",
        ascending=False
    )

    print("\nFeature Importance")
    print(importance)

    importance.to_csv(
        "outputs/feature_importance.csv",
        index=False
    )

    # Generate Feature Importance Plot
    plt.figure(figsize=(8, 5))

    plt.barh(
        importance["Feature"][::-1],
        importance["Importance"][::-1]
    )

    plt.xlabel("Importance")
    plt.ylabel("Feature")
    plt.title("Random Forest Feature Importance")

    plt.tight_layout()

    plt.savefig(
        "outputs/feature_importance.png",
        dpi=300, bbox_inches="tight"
    )

    plt.close()

    print(
        "Saved: outputs/feature_importance.png"
    )

    print(
        classification_report(
            y_test,
            preds
        )
    )

    return model