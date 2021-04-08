// Generated by gencpp from file moveit_msgs/GetCartesianPath.msg
// DO NOT EDIT!


#ifndef MOVEIT_MSGS_MESSAGE_GETCARTESIANPATH_H
#define MOVEIT_MSGS_MESSAGE_GETCARTESIANPATH_H

#include <ros/service_traits.h>


#include <moveit_msgs/GetCartesianPathRequest.h>
#include <moveit_msgs/GetCartesianPathResponse.h>


namespace moveit_msgs
{

struct GetCartesianPath
{

typedef GetCartesianPathRequest Request;
typedef GetCartesianPathResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct GetCartesianPath
} // namespace moveit_msgs


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::moveit_msgs::GetCartesianPath > {
  static const char* value()
  {
    return "2f81861c2a157da4ea888c0db053e2a1";
  }

  static const char* value(const ::moveit_msgs::GetCartesianPath&) { return value(); }
};

template<>
struct DataType< ::moveit_msgs::GetCartesianPath > {
  static const char* value()
  {
    return "moveit_msgs/GetCartesianPath";
  }

  static const char* value(const ::moveit_msgs::GetCartesianPath&) { return value(); }
};


// service_traits::MD5Sum< ::moveit_msgs::GetCartesianPathRequest> should match
// service_traits::MD5Sum< ::moveit_msgs::GetCartesianPath >
template<>
struct MD5Sum< ::moveit_msgs::GetCartesianPathRequest>
{
  static const char* value()
  {
    return MD5Sum< ::moveit_msgs::GetCartesianPath >::value();
  }
  static const char* value(const ::moveit_msgs::GetCartesianPathRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::moveit_msgs::GetCartesianPathRequest> should match
// service_traits::DataType< ::moveit_msgs::GetCartesianPath >
template<>
struct DataType< ::moveit_msgs::GetCartesianPathRequest>
{
  static const char* value()
  {
    return DataType< ::moveit_msgs::GetCartesianPath >::value();
  }
  static const char* value(const ::moveit_msgs::GetCartesianPathRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::moveit_msgs::GetCartesianPathResponse> should match
// service_traits::MD5Sum< ::moveit_msgs::GetCartesianPath >
template<>
struct MD5Sum< ::moveit_msgs::GetCartesianPathResponse>
{
  static const char* value()
  {
    return MD5Sum< ::moveit_msgs::GetCartesianPath >::value();
  }
  static const char* value(const ::moveit_msgs::GetCartesianPathResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::moveit_msgs::GetCartesianPathResponse> should match
// service_traits::DataType< ::moveit_msgs::GetCartesianPath >
template<>
struct DataType< ::moveit_msgs::GetCartesianPathResponse>
{
  static const char* value()
  {
    return DataType< ::moveit_msgs::GetCartesianPath >::value();
  }
  static const char* value(const ::moveit_msgs::GetCartesianPathResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // MOVEIT_MSGS_MESSAGE_GETCARTESIANPATH_H
