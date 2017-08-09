import os
from atomate.vasp.powerups import use_fake_vasp


def vasp_emulator(wf, ref_dir="/wkshp_shared/workshop_ref_files", calc="electronic_structure"):
    reference_dir = os.path.join(os.path.expanduser(ref_dir), calc)
    params_to_check = None
    
    if calc == "electronic_structure":

        ref_dirs = {
            "structure optimization": os.path.join(reference_dir, "Si_structure_optimization"),
            "static": os.path.join(reference_dir, "Si_static"),
            "nscf uniform": os.path.join(reference_dir, "Si_nscf_uniform"),
            "nscf line": os.path.join(reference_dir, "Si_nscf_line")
        }
        
    elif calc == "elastic_tensor":

        ref_dirs = {
            "structure optimization": os.path.join(reference_dir, "1"),
            "elastic deformation 0": os.path.join(reference_dir, "7"),
            "elastic deformation 1": os.path.join(reference_dir, "6"),
            "elastic deformation 2": os.path.join(reference_dir, "5"),
            "elastic deformation 3": os.path.join(reference_dir, "4"),
            "elastic deformation 4": os.path.join(reference_dir, "3"),
            "elastic deformation 5": os.path.join(reference_dir, "2")
        }
        params_to_check=["ENCUT"]

    else:
        raise ValueError("wrong 'calc' option")
        
    return use_fake_vasp(wf, ref_dirs, params_to_check=params_to_check)


def get_task_id(lp, fw_name):
    for fw_id in lp.get_fw_ids():
        fw=lp.get_fw_by_id(fw_id)
        if fw.name == fw_name:
            return fw.launches[-1].action.stored_data["task_id"]
    return None
