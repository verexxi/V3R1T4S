# Exact commands (run from a folder holding the files of this directory under src/, and data_cache/ as in the run)
python src/mkxyz.py Li      # fit/val/train_all extxyz from the benchmark json + jarvis 'mlearn' structures
# selection on val only (selection_on_val.txt), then the final seeds on all train ids (seeds 1, 2, 3):
BS=3 LR=0.005 sh src/launch.sh jobs/Li_final_s1 2 14400 work/Li/train_all.xyz work/Li/val.xyz 1 150 32 4.5
python src/evaluate_final.py Li jobs/Li_final      # test scored once: 3 seeds + ensemble
Training: 2 CPU threads per job, float32; inference float64 (predict.py).
