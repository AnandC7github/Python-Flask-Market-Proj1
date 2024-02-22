from market import app, db
from market.models import Item, User

if __name__ == '__main__':
    with app.app_context():
        item_to_update = Item.query.get(2)

        items_to_delete = Item.query.filter(Item.id.between(2, 14)).all()
        for item in items_to_delete:
            db.session.delete(item)
        db.session.commit()

        print(__name__)
        app.run(host="0.0.0.0", port=3000, debug=True)