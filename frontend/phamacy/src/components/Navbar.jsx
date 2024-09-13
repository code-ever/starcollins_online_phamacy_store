import React from 'react'
import { FaRegUser } from "react-icons/fa";
import { FiSearch } from "react-icons/fi";
import { IoCartOutline } from "react-icons/io5";


function Navbar() {
    return (
        <div className='flex justify-between items-center py-2 px-4 pt-16'>
            <div>logo</div>
            <div className='hidden md:flex'>
                <div className='flex items-center w-[500px] border border-1 border-red-600 p-2 rounded-md'>
                    <input type="text" placeholder='Search.....' className='w-full' />
                    <p className=''>
                        <FiSearch className='' size={30} />
                    </p>

                </div>
            </div>
            
            <div className='flex items-center px-2 gap-x-4'>
                <p>
                    <FiSearch className='flex md:hidden' size={30} />
                </p>
                <FaRegUser className='cursor-pointer' size={25} />
                <IoCartOutline className='cursor-pointer' size={25} />
            </div>
        </div>
    )
}

export default Navbar
