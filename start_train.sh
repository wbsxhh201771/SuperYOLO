python train.py --cfg models/SRyolo_MF.yaml --super --train_img_size 1024 --hr_input --data data/Fire_Smoke.yaml --ch 64 --input_mode RGB+IR+MF --batch-size 2 --device 0
python train.py --cfg models/SRyolo_MF.yaml --train_img_size 512 --hr_input --data data/Fire_Smoke.yaml --ch 64 --input_mode RGB+IR+MF --batch-size 8 --device 0
python train.py --cfg models/SRyolo_noFocus_small.yaml --train_img_size 512 --data data/Fire_Smoke_kaggle.yaml --ch 3 --input_mode RGB --batch-size 2 --device 0
# python train.py --cfg models/SRyolo_MF.yaml --super --train_img_size 1024 --hr_input --data data/Fire_Smoke_kaggle.yaml --ch 64 --input_mode RGB+IR+MF --batch-size 2 --device 0
python train.py --cfg models/SRyolo_MF.yaml --super --train_img_size 1024 --hr_input --data data/Fire_Smoke_kaggle_400.yaml --ch 64 --input_mode RGB+IR+MF --batch-size 2 --device 0
python train.py --cfg models/SRyolo_MF.yaml --super --train_img_size 1024 --hr_input --data data/Fire_Smoke.yaml --ch 64 --input_mode RGB+IR+MF --batch-size 4 --device 0
python train.py --cfg models/SRyolo_MF.yaml --train_img_size 512 --data data/Fire_Smoke.yaml --ch 64 --input_mode RGB+IR+MF --batch-size 8 --device 0
python train.py --cfg models/SRyolo_MF.yaml --super --train_img_size 1024 --hr_input --data data/Small_Fire_Smoke.yaml --ch 64 --input_mode RGB+IR+MF --batch-size 8 --device 0
tensorboard --logdir=train
python train.py --cfg models/SRyolo_MF.yaml --super --train_img_size 1024 --hr_input --data data/Small_Fire_Smoke_1024.yaml --ch 64 --input_mode RGB+IR+MF --batch-size 8 --device 0
python train.py --cfg models/SRyolo_noFocus_small.yaml --super --train_img_size 1024 --hr_input --data data/Small_Fire_Smoke_1024.yaml --ch 3 --input_mode RGB --batch-size 8 --device 0
python train.py --cfg models/SRyolo_MF_Fire.yaml --super --train_img_size 1024 --hr_input --data data/Fire_Car.yaml --ch 64 --input_mode RGB+IR+MF --batch-size 8 --device 0
sudo nvidia-smi -i 1 -pl 200
tensorboard --logdir runs/train
python train.py --cfg models/SRyolo_noFocus_small_Fire.yaml --super --train_img_size 1024 --hr_input --data data/Fire_Car.yaml --ch 3 --input_mode RGB --batch-size 8 --device 0
python test.py --data data/Fire_Car_test.yaml --weights runs/train/exp6/weights/best.pt --input_mode RGB+IR+MF
python test.py --weights weights/RGB+IR+MF_super_1024.pt --input_mode RGB+IR+MF --data data/SRvedai.yaml
python train.py --cfg models/SRyolo_MF_Fire_Smoke_v8.yaml --train_img_size 512 --data data/SRvedai.yaml --ch 3 --input_mode RGB > logs/v8_dwconv_RGB_log.txt 2>&1
python train.py --cfg models/SRyolo_MF_Fire_Smoke_v8.yaml --train_img_size 512 --data data/SRvedai.yaml --ch 3 --input_mode IR > logs/v8_dwconv_IR_log.txt 2>&1
python train.py --cfg models/SRyolo_MF_Fire_Smoke_v8_dwconv.yaml --train_img_size 512 --data data/FASDD_CV.yaml --ch 64 --input_mode RGB+IR+MF --batch-size 8 --device 0 > logs/v8_dwconv_RGB+IR+MF_log.txt 2>&1
python test.py --data data/Fire_Car_test.yaml --weights weights/expv11_RGB+IR+MF/v11DWCONV_RGB_IR_RIMF/weights/best.pt --input_mode RGB+IR+MF
nohup python train.py --cfg models/SRyolo_MF_Fire_Smoke_v11_dwconv.yaml --train_img_size 512 --data data/Fire_Car_test.yaml --ch 64 --input_mode RGB+IR+MF --batch-size 16 --device 0 > logs/rimf_v11_dwconv_RGB+IR+MF_log.txt 2>&1 & tail -f logs/rimf_v11_dwconv_RGB+IR+MF_log.txt
python train.py --cfg models/SRyolo_MF_Fire_Smoke_v11_dwconv.yaml --train_img_size 512 --data data/FASDD_CV.yaml --ch 64 --input_mode RGB+IR+MF --batch-size 16 --device 0 --weights runs/train/v11DWCONV_RGB_IR_RIMF/weights/best.pt  > logs/rimf2_v11_dwconv_RGB+IR+MF_log.txt 2>&1
