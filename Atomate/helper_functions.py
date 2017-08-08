import os
from atomate.vasp.powerups import use_fake_vasp


def electronic_structure_simulator(wf, ref_dir="/wkshp_shared/workshop_ref_files/electronic_structure"):
    reference_dir = os.path.expanduser(ref_dir)
    ref_dirs_si = {
        "structure optimization": os.path.join(reference_dir, "Si_structure_optimization"),
        "static": os.path.join(reference_dir, "Si_static"),
        "nscf uniform": os.path.join(reference_dir, "Si_nscf_uniform"),
        "nscf line": os.path.join(reference_dir, "Si_nscf_line")
    }
    
    return use_fake_vasp(wf, ref_dirs_si)


def elastic_simulator(wf, ref_dir="/wkshp_shared/workshop_ref_files/elastic_tensor"):
    reference_dir = os.path.expanduser(ref_dir)

    si_ref_dirs = {
        "structure optimization": os.path.join(reference_dir, "1"),
        "elastic deformation 0": os.path.join(reference_dir, "7"),
        "elastic deformation 1": os.path.join(reference_dir, "6"),
        "elastic deformation 2": os.path.join(reference_dir, "5"),
        "elastic deformation 3": os.path.join(reference_dir, "4"),
        "elastic deformation 4": os.path.join(reference_dir, "3"),
        "elastic deformation 5": os.path.join(reference_dir, "2")
    }

    return use_fake_vasp(wf, si_ref_dirs, params_to_check=["ENCUT"])


def get_task_id(lp, fw_name):
    for fw_id in lp.get_fw_ids():
        fw=lp.get_fw_by_id(fw_id)
        if fw.name == fw_name:
            return fw.launches[-1].action.stored_data["task_id"]
    return None
