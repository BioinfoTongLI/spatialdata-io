import fire
from pathlib import Path
from spatialdata_io.readers import codex, cosmx, curio, iss, mcmicro, merscope, metaspace, resolve, steinbock, visium, xenium

def main(input_folder:str, technology:str, out_dir:str, **write_options)->None:
    """
    Main function to process spatial data based on the given technology.

    :param input_folder: The input folder containing the data to process
    :type input_folder: str
    :param technology: The technology flag indicating which reader to use
    :type technology: str
    :raises ValueError: If an invalid technology flag is provided
    """
    # Ensure the input is a Path object
    input_folder = Path(input_folder)
    technology = technology.lower().strip()

    # Depending on the technology flag, use the corresponding reader function
    if technology == 'codex':
        data = codex.codex(input_folder)
    elif technology == 'cosmx':
        data = cosmx.cosmx(input_folder)
    elif technology == 'curio':
        data = curio.curio(input_folder)
    elif technology == 'iss':
        data = iss.iss(input_folder)
    elif technology == 'mcmicro':
        data = mcmicro.mcmicro(input_folder)
    elif technology == 'merscope':
        data = merscope.merscope(input_folder)
    elif technology == 'metaspace':
        data = metaspace.metaspace(input_folder)
    elif technology == 'resolve':
        data = resolve.resolve(input_folder)
    elif technology == 'steinbock':
        data = steinbock.steinbock(input_folder)
    elif technology == 'visium':
        data = visium.visium(input_folder)
    elif technology == 'xenium':
        data = xenium.xenium(input_folder)
    else:
        raise ValueError(f"Technology {technology} is not supported yet")

    # Write the data to the output directory
    data.write(out_dir, **write_options)

if __name__ == "__main__":
    fire.Fire(main)