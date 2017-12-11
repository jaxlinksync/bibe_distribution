mkdir datas
cp ~/latest_features/numpy_features/* datas/
python generate_txt.py datas/
python distribute.py distribution.txt numpy_features numpy_features_valid 0.93
mkdir scarlet_johanson
cp -r norm_info/ scarlet_johanson/
cp -r numpy_features/ scarlet_johanson/
cp -r numpy_features_valid/ scarlet_johanson/
