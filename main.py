from market import app, db
from market.models import Item, User

if __name__ == '__main__':
    with app.app_context():
        # Adding a new item - Office Chair
        office_chair = Item(
            name='Office Chair',
            barcode='96573029468394',
            price=25000,
            description='A comfortable and ergonomic office chair designed to provide optimal support and style for your workspace. This chair features: - High-quality materials for durability and longevity. - Adjustable seat height and armrests for personalized comfort. - Lumbar support to maintain a healthy posture during long hours of work. - Smooth swivel and casters for easy mobility. - Stylish design to enhance the aesthetics of your office.'
        )
        db.session.add(office_chair)
        db.session.commit()

        print(__name__)
        app.run(host="0.0.0.0", port=3000, debug=True)