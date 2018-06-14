
# development config

dev_csv_fd = "/home/ruksana/test/DCASE2016_Task1/tools/TUT-acoustic-scenes-2016-development/evaluation_setup"

dev_tr_csv = [dev_csv_fd+"/fold1_train.txt", dev_csv_fd+"/fold2_train.txt", 
               dev_csv_fd+"/fold3_train.txt", dev_csv_fd+"/fold4_train.txt"]

dev_te_csv = [dev_csv_fd+"/fold1_evaluate.txt", dev_csv_fd+"/fold2_evaluate.txt", 
               dev_csv_fd+"/fold3_evaluate.txt", dev_csv_fd+"/fold4_evaluate.txt"]
dev_meta_csv = "/home/ruksana/test/DCASE2016_Task1/tools/TUT-acoustic-scenes-2016-development/meta.txt"


# evaluation config
eva_meta_csv = "/home/ruksana/test/DCASE2016_Task1/tools/TUT-acoustic-scenes-2016-evaluation/meta.txt"


#BACKUP FILES FDS#####################

# development config

bdev_csv_fd = "/home/ruksana/test/DCASE2016_Task1/tools/TUT-acoustic-scenes-2016-development/evaluation_setup"

bdev_tr_csv = [dev_csv_fd+"/fold1_train.backup.txt", dev_csv_fd+"/fold2_train.backup.txt", 
               dev_csv_fd+"/fold3_train.backup.txt", dev_csv_fd+"/fold4_train.backup.txt"]

bdev_te_csv = [dev_csv_fd+"/fold1_evaluate.backup.txt", dev_csv_fd+"/fold2_evaluate.backup.txt", 
               dev_csv_fd+"/fold3_evaluate.backup.txt", dev_csv_fd+"/fold4_evaluate.backup.txt"]
bdev_meta_csv = "/home/ruksana/test/DCASE2016_Task1/tools/TUT-acoustic-scenes-2016-development/meta.backup.txt"


# evaluation config
beva_meta_csv = "/home/ruksana/test/DCASE2016_Task1/tools/TUT-acoustic-scenes-2016-evaluation/meta.backup.txt"

############################

labels = ['bus', 'cafe/restaurant', 'car', 'city_center', 'forest_path', 
           'grocery_store', 'home', 'beach', 'library', 'metro_station', 
           'office', 'residential_area', 'train', 'tram', 'park']