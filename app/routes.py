from app import app, db
from flask import jsonify, request
from app.models import Ad


@app.route('/ads', methods=['POST'])
def create_ad():
    data = request.json
    new_ad = Ad(
        title=data['title'],
        description=data['description'],
        owner=data['owner']
    )
    db.session.add(new_ad)
    db.session.commit()
    return jsonify({"message": "Объявление создано", "ad_id": new_ad.id}), 201


@app.route('/ads/<int:id>', methods=['GET'])
def get_ad(id):
    ad = Ad.query.get_or_404(id)
    return jsonify({
        'id': ad.id,
        'title': ad.title,
        'description': ad.description,
        'created_at': ad.created_at,
        'owner': ad.owner
    })


@app.route('/ads/<int:id>', methods=['PUT'])
def update_ad(id):
    ad = Ad.query.get_or_404(id)
    data = request.json
    ad.title = data.get('title', ad.title)
    ad.description = data.get('description', ad.description)
    db.session.commit()
    return jsonify({"message": "Объявление обновлено"}), 200


@app.route('/ads/<int:id>', methods=['DELETE'])
def delete_ad(id):
    ad = Ad.query.get_or_404(id)
    db.session.delete(ad)
    db.session.commit()
    return jsonify({"message": "Объявление удалено"}), 200
