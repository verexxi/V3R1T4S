# Exact commands (run from a folder holding the files of this directory under src/, and data_cache/ as in the run)
python src/mkxyz.py Si      # fit/val/train_all extxyz from the benchmark json + jarvis 'mlearn' structures
# selection on val only (selection_on_val.txt), then the final seeds on all train ids (seeds 1, 2, 3):
BS=3 LR=0.005 sh src/launch.sh jobs/Si_final_s1 2 14400 work/Si/train_all.xyz work/Si/val.xyz 1 150 16 4.5
python src/evaluate_final.py Si jobs/Si_final      # test scored once: 3 seeds + ensemble
Training: 2 CPU threads per job, float32; inference float64 (predict.py).
