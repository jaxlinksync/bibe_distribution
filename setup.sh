mkdir datas
cp ~/latest_features/numpy_features/* datas/
python generate_txt.py datas/
python distribute.py distribution.txt numpy_features numpy_features_valid 0.93
rm -rf datas
